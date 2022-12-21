import requests
import json
import sys
import configparser

config = configparser.ConfigParser()
config.read('configration.ini')
domain = sys.argv[1]
API_KEY = config['api']['key']

response = requests.get(f"https://crt.sh/?q=%.{domain}&output=json")

data = json.loads(response.text)

subdomains_crt = [entry["name_value"] for entry in data]

response = requests.get(f"https://api.securitytrails.com/v1/domain/{domain}/subdomains?apikey={API_KEY}")

data = json.loads(response.text)

subdomains_securitytrails = [subdomain + f".{domain}" for subdomain in data["subdomains"]]

subdomains = subdomains_crt + subdomains_securitytrails

subdomains = [subdomain for subdomain in subdomains if "*" not in subdomain]

for subdomain in subdomains:
    print(subdomain)

# SUBJ - Subdomain Finder

![Build](https://img.shields.io/badge/Built%20with-Python-Blue)
[![Twitter](https://img.shields.io/twitter/follow/sl0wh_py?label=Follow)](https://twitter.com/sl0wh_py)

> A simple subdomain finder

Thanks to @GodfatherOrwa methodology about recon, this tool bring subdomains from https://crt.sh & https://securitytrails.com.

**Here** you can download @GodfatherOrwa methodology about recon https://www.houseofhackers.xyz/t/recon-skills-and-tips-by-god-father-orwa-iwcon-w2022-talk-slides/25.

**subj** is being actively developed by [@sl0wh_py](https://twitter.com/sl0wh_py)

Installation & Usage
------------
**Requirement: python 3.x**
```
git clone https://github.com/slowhpy/SUBJ.git
```

API_KEY (IMPORTANT)
---------------

- you should have an account in https://securitytrails.com.
- open configration file and add your securitytrails API_KEY.
```
cd SUBJ
vim configration.ini
```

How to use
---------------

```
python3 subj.py target
```
```
python3 subj.py example.com
```
### Delete Duplicate
```
python3 subj.py example.com | sort -u
```

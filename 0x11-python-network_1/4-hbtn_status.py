#!/usr/bin/python3
""" Fetches https://alx-intranet.hbtn.io/status
"""
import requests

url = "https://alx-intranet.hbtn.io/status"
rspns = requests.get(url)
print("Body response:")
print("\t- type:", type(rspns.text))
print("\t- content:", rspns.text)

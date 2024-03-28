#!/usr/bin/python3
"""
takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""
from urllib.request import HTTPBasicAuthHandler
import requests
import sys

if __name__ == "__main__":
    Auth = HTTPBasicAuthHandler(sys.argv[1], sys.argv[2])
    rspns = requests.get("https://api.github.com/user", auth=Auth)
    print(rspns.json().get("id"))

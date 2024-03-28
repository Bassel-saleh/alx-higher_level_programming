#!/usr/bin/python3
"""
takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""
import requests
import sys

if __name__ == "__main__":
    usr = sys.argv[1]
    passcode = sys.argv[2]
    url = "https://api.github.com/user"
    auth = (usr, passcode)
    rspns = requests.get(url, auth=auth)
    if rspns.status_code == 200:
        usr_info = rspns.json()
        usr_id = usr_info['id']
        print(usr_id)
    else:
        print(None)

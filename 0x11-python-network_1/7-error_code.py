#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL
and displays the body of the response
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    rspns = requests.get(url)
    if rspns.status_code >= 400:
        print("Error code:", rspns.status_code)
    else:
        print(rspns.text)

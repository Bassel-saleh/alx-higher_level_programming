#!/usr/bin/python3
"""
Takes in a URL and an email
sends a POST request to the passed URL with the email as a parameter
and displays the body of the response (decoded in utf-8)
"""
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    mail = {"email": sys.argv[2]}
    t = urllib.parse.urlencode(mail).encode("utf-8")
    r = urllib.request.Request(url, t)
    with urllib.request.urlopen(r) as rspns:
        print(rspns.read().decode("utf-8"))

#!/usr/bin/python3
"""
takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter
"""
import requests
import sys

if __name__ == "__main__":
    if len (sys.argv) > 1:
        letter = sys.argv[1]
    else:
        letter = ""
    d = {'q': letter}
    rspns = requests.post("http://0.0.0.0:5000/search_user", data=d)
    try:
        json_rspns = rspns.json()
        if json_rspns:
            print("[{}] {}".format(json_rspns.get("id"), json_rspns.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")

#!/usr/bin/python3
"""
script that passes a letter parameter to a URL and returns the
response body when its properly JSON formatted
"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]

    payload = {'q': q}
    url = "http://0.0.0.0:5000/search_user"
    req = requests.post(url, data=payload)

    try:
        res = req.json()
        if res == {}:
            print('No result')
        else:
            print(f"[{res.get('id')}] {res.get('name')}")
    except ValueError:
        print('Not a valid JSON')

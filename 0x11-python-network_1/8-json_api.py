#!/usr/bin/python3
"""
script that passes a letter parameter to a URL and returns the
response body when its properly JSON formatted
"""
import requests
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    q = str(sys.argv[1])
    if q == None:
        q = ""
        print("No result")
    elif q != type(str):
        print("No result")
    else:
        req = requests.post(url, data=q.encode('utf-8'))
        print(f"[{q.id}] {q.name}")

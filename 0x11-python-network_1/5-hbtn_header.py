#!/usr/bin/python3
""" module to display variable value in response header from a given URL """
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        req = requests.get(url)
        print(req.headers['X-Request-Id'])
    except True:
        pass
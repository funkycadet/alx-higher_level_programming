#!/usr/bin/python3
""" module to display variable value in response header from a given URL """
import requests
import sys

if __name__ == "__main__":
    try:
        url = sys.argv[1]
        req = requests.get(url)
        print(req.headers['X-Request-Id'])
    except requests.RequestException:
        pass

#!/usr/bin/python3
""" module to display header value found in response header """
import sys
import urllib.request

if __name__ == "__main__":
    req = sys.argv[1]
    with urllib.request.urlopen(req) as response:
        print(response.headers['X-Request-Id'])

#!/usr/bin/python3
""" module to display variable value in response header from a given URL """
import requests
import sys

url = sys.argv[1]
req = requests.request('GET', url)
print(req.headers['X-Request-Id'])

#!/usr/bin/python3
"""
script to send a POST request using an email address as a parameter
to a URL and display the response body
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    req = requests.post(url, data={'email': sys.argv[2]})

    print(req.text)

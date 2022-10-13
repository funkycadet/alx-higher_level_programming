#!/usr/bin/python3
""" module to fetch status from url """
import urllib.request

if __name__ == "__main__":
    req = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(req) as request:
        response = request.read()
        print("Body response:")
        print("\t- type: {}".format(type(response)))
        print("\t- content: {}".format(response))
        print("\t- utf8 content: {}".format(response.decode('UTF-8')))

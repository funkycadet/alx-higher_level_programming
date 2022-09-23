#!/usr/bin/python3
"""
module to return response body of passed URL decoded in utf-8
"""
import sys
from urllib import request, error

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with request.urlopen(url) as response:
            print(response)
    except error.HTTPError as e:
        print(f"Error code: {e.code}")

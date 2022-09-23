#!/usr/bin/python3
"""
module to return response body of passed URL decoded in utf-8
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        req = requests.get(url)
        print(f"Error code: {req.status_code}")
    except req.raise_for_status as e:
        print(f"Error code: {req.status_code}")

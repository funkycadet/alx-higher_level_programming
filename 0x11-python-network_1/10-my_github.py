#!/usr/bin/python3
"""
Takes my GitHub credentials and uses
the GitHub API to display my ID
"""

import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    url = "https://api.github.com/user"

    token = HTTPBasicAuth(username, password)
    req = requests.get(url, auth=token)
    print(req.json().get('id'))

#!/bin/bash
# Script to send a GET request to a URL argument and display response body
curl -X GET -H "X-School-User-Id: 98" "$1"

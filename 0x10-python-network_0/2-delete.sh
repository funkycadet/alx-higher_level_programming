#!/bin/bash
# Script to send a DELETE request to a URL passed as argument and display response body
curl -s "$1" -X DELETE

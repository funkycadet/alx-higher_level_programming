#!/bin/bash
# Script to display all HTTP methods a server will accept from a URL
curl -sI -X OPTIONS "$1" | grep "Allow:" | cut -d " " -f 2-

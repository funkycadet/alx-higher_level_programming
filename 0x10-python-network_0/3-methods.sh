#!/bin/bash
# Script to display all HTTP methods a server will accept from a URL
curl -i -L -X OPTIONS $1

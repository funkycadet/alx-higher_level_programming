#!/bin/bash
# Script to display the size of a URL body response
curl -so /dev/null $1 -w '%{size_download}'

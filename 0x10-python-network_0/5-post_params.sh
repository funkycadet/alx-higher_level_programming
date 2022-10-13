#!/bin/bash
# Script to send POST request and display values
curl -s "$1" -X POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD"

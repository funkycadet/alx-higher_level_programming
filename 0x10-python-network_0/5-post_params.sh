#!/bin/bash
# Script to send POST request and display values
curl  -d "email=test@gmail.com&subject=I will always be here for PLD" -X POST "$1"

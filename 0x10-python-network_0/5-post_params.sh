#!/bin/bash
# Script to send POST request and display values
curl -sL "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"

#!/bin/bash
# Make a POST request with email and subject as params

# Check if the number of arguments is correct
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Assign URL to a variable
URL="$1"

# Make the POST request using curl
curl -s -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$URL"

#!/bin/bash
# Send the required POST parameters and display the response body.
curl -s -X POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"

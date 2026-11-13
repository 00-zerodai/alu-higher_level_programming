#!/usr/bin/python3
"""Fetch a URL and display its body or HTTP error status."""
import sys
import requests


if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)

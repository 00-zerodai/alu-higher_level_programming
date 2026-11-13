#!/usr/bin/python3
"""Display the authenticated GitHub user's identifier."""
import sys
import requests


if __name__ == "__main__":
    response = requests.get(
        "https://api.github.com/user",
        auth=(sys.argv[1], sys.argv[2]))
    print(response.json().get("id"))

#!/usr/bin/python3
"""Display the X-Request-Id response header for a requested URL."""
import sys
import requests


if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    print(response.headers.get("X-Request-Id"))

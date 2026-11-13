#!/usr/bin/python3
"""Submit a letter to the search API and display its JSON response."""
import sys
import requests


if __name__ == "__main__":
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    response = requests.post(
        "http://0.0.0.0:5000/search_user", data={"q": letter})
    try:
        result = response.json()
    except ValueError:
        print("Not a valid JSON")
    else:
        if result:
            print("[{}] {}".format(result.get("id"), result.get("name")))
        else:
            print("No result")

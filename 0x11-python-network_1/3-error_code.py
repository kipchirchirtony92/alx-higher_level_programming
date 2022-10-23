#!/usr/bin/env python3
"""Sends a request to a given URL and displays the response body.
Usage: ./3-error_code.py <URL>
  - Handles HTTP errors.
"""

import urllib.request
from sys import argv

if __name__ == "__main__":
    url = argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode("UTF-8"))
    except urllib.error.HTTPError as e:
        print(f"Error code : {e.code}")

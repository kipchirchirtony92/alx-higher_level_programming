#!/usr/bin/env python3
""" Script takes in a URL sends a request using the urllib and displays
 the X-Request-Id variable found in the header of the response
  only import sys and urllib
"""
import urllib.request
from sys import argv

if __name__ == "__main__":
    url = argv[1]

    with urllib.request.urlopen(url) as response:
        print(dict(response.headers).get("X-Request-Id"))

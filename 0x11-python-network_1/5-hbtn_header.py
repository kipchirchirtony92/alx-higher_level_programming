#!/usr/bin/env python3
"""Displays the X-Request-Id header variable of a request to a given URL.
Usage: ./5-hbtn_header.py <URL>
"""
import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]

    response = requests.get(url)
    print(response.headers.get("X-Request-Id"))

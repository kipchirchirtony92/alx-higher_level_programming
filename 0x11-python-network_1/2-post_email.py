#!/usr/bin/env python3
""" script takes in a URL and an email, sends a POST request to the
 passed URL with the email as a parameter and displays the body of
 the response decode in 'utf-8'
"""
import urllib.request
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    param = {"email": argv[2]}
    data = urllib.parse.urlencode(param).encode('ascii')

    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("UTF-8"))

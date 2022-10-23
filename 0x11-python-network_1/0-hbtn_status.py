#!/usr/bin/env python3
"""
 Fetches form the URL
  https://intranet.hbtn.io/status using the urllib package
"""

import urllib.request

if __name__ == "__main__":

    with urllib.request.urlopen("https://intranet.hbtn.io/status") as request:
        resp = request.read()
        print("Body response:")
        print("\t- type: {}".format(type(resp)))
        print("\t- content: {}".format(resp))
        print("\t- utf8 content: {}".format(resp.decode("UTF-8")))

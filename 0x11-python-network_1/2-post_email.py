#!/usr/bin/python3
"""
This Python script sends a POST request to a URL with an email parameter
and displays the body of the response.
"""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    data = urllib.parse.urlencode({"email": sys.argv[2]}).encode("ascii")
    fetch_url = urllib.request.Request(sys.argv[1], data)

    with urllib.request.urlopen(fetch_url) as response:
        print(response.read().decode("utf-8"))

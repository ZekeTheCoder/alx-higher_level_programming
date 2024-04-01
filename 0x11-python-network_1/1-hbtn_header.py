#!/usr/bin/python3
"""
This Python script sends a request to a URL and displays the value of
the X-Request-Id variable found in the header of the response.
"""
import urllib.request
import sys


if __name__ == "__main__":
    fetch_url = urllib.request.Request(sys.argv[1])

    with urllib.request.urlopen(fetch_url) as response:
        print(response.getheader("X-Request-Id"))

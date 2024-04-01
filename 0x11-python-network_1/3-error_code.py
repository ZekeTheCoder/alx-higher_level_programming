#!/usr/bin/python3
"""
This Python script sends a request to a URL
and displays the body of the response (decoded in utf-8).
"""
import urllib.request
import urllib.error
import sys


if __name__ == "__main__":
    fetch_url = sys.argv[1]

    try:
        with urllib.request.urlopen(fetch_url) as response:
            print(response.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))

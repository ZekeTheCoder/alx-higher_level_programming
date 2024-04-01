#!/usr/bin/python3
"""
This Python script takes in a URL, sends a request to the URL
and displays the value of the variable X-Request-Id in the response header.
"""
import requests
import sys


if __name__ == "__main__":
    fetch_url = requests.get(sys.argv[1])
    print(fetch_url.headers.get("X-Request-Id"))

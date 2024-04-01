#!/usr/bin/python3
"""
This Python script fetches https://alx-intranet.hbtn.io/status
and displays the body of the response.
"""
import requests


if __name__ == "__main__":
    fetch_url = requests.get("https://alx-intranet.hbtn.io/status")

    print("Body response:")
    print("\t- type: {}".format(type(fetch_url.text)))
    print("\t- content: {}".format(fetch_url.text))

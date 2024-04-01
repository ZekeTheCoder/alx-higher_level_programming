#!/usr/bin/python3
"""
This Python script takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        letter = ""
    else:
        letter = sys.argv[1]

    fetch_url = requests.post("http://0.0.0.0:5000/search_user", {'q': letter})

    try:
        response = fetch_url.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))

    except ValueError:
        print("Not a valid JSON")

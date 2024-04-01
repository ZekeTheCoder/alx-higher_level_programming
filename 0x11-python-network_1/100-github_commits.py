#!/usr/bin/python3
"""
This Python script lists 10 commits (from the most recent to oldest)
of a specified repository by a given owner using the GitHub API.
"""
import requests
import sys


if __name__ == "__main__":
    fetch_url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    result = requests.get(fetch_url)
    commits = result.json()

    try:
        for i in range(10):
            print("{}: {}".format(
                commits[i].get("sha"),
                commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass

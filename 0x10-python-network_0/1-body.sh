#!/bin/bash
# This Bash script takes a URL as input, sends a GET request, and displays the body of the response (for 200 status code only)
curl -s -L "$1"

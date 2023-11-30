#!/usr/bin/python3
import sys

if __name__ == "__main__":
    i = len(sys.argv) - 1

    if i == 0:
        print("{} arguments.".format(i))
    elif i == 1:
        print("{} argument:".format(i))
    else:
        print("{} arguments:".format(i))

    for i, arg in enumerate(sys.argv[1:], start=1):
        print("{}: {}".format(i, arg))

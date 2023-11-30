#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    for attribute in dir(hidden_4):
        if attribute[0:2] != "__":
            print(attribute)

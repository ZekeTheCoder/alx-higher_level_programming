#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        character = ord(str[i])
        if 97 <= character <= 122:
            character = character - 32
            str = str[:i] + chr(character) + str[i + 1:]
    print("{}".format(str))

#!/usr/bin/python3
def remove_char_at(str, n):
    string_copy = ""
    for i in range(len(str)):
        if i != n:
            string_copy = string_copy + str[i]
    return (string_copy)

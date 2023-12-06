#!/usr/bin/python3
def number_keys(a_dictionary):
    num = 0
    dict_keys = list(a_dictionary.keys())
    for i in dict_keys:
        num += 1
    return (num)

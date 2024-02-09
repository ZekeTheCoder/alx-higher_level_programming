#!/usr/bin/python3
def magic_string(separator=', '):
    magic_string.n = getattr(magic_string, 'n', 0) + 1
    return ("BestSchool" + separator) * magic_string.n

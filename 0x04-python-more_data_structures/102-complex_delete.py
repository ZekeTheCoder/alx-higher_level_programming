#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys_to_keep = [key for key, val in a_dictionary.items() if val != value]
    new_dict = {key: a_dictionary[key] for key in keys_to_keep}

    return (new_dict)

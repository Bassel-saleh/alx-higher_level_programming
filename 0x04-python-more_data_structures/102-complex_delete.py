#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for k in a_dictionary.keys():
        if a_dictionary[k] == value:
            del a_dictionary[key]
    return a_dictionary

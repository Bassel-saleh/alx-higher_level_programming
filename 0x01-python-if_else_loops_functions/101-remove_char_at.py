#!/usr/bin/python3
def remove_char_at(str, n):
    tmp = ""
    for i, c in enumerate(str):
        if i != n:
            tmp += c
    return tmp

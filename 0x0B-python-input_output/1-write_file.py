#!/usr/bin/python3
''' Module for writing a text in a file '''


def write_file(filename="", text=""):
    ''' writes text in a file '''
    with open(filename, encoding=utf-8) as f:
        return f.write(text)

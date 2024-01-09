#!/usr/bin/python3
'''read_file function '''


def read_file(filename=""):
    ''' reads filename with utf-8 '''
    with open(fiename, encoding='utf-8') as f:
        print(f.read(), end="")

#!/usr/bin/python3
""" lookup method """


def lookup(obj):
    ''' looks up obj attribute methods
    Args:
        obj: the class object

    Returns:
        list: list of attributes
    '''
    return dir(obj)

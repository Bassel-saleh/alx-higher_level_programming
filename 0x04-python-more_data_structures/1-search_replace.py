#!/usr/bin/python3
def search_replace(my_list, search, replace):
    n = list(map(lambda c: replace if c == search else c, my_list))
    return n

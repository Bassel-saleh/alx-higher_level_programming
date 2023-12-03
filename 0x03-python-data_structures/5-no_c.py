#!/usr/bin/env python3
def no_c(my_string):
    noc_str = ""
    for i in range(len(my_string)):
        if my_string[i] != 'c' and my_string[i] != 'C':
            noc_str += my_string[i]
    return noc_str

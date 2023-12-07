#!/usr/bin/python3'
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    t = 0
    n = 0
    r_digits = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for x in (roman_string):
        n = r_digits[x]
        t += n
    return t
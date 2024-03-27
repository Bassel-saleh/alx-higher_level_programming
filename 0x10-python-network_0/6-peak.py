#!/usr/bin/python3
""" finds the peak in a list
"""


def find_peak(list_of_integers):
    """finds the peak in a list of integers

    Args:
        list_of_integers (list): the list to be checked
    """
    if list_of_integers is None or list_of_integers == []:
        return None
    low = 0
    length = len(list_of_integers)
    mid = ((length - low) / 2) + low
    mid = int(mid)
    if length == 1:
        return list_of_integers[0]
    if length == 2:
        return max(list_of_integers)
    if list_of_integers[mid] >= list_of_integers[mid - 1] and\
            list_of_integers[mid] >= list_of_integers[mid + 1]:
        return list_of_integers[mid]
    if mid > 0 and list_of_integers[mid] < list_of_integers[mid + 1]:
        return find_peak(list_of_integers[mid:])
    if mid > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])

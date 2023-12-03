#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is None:
        return None
    w_list = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            w_list.append(True)
        else:
            w_list.append(False)
    return w_list

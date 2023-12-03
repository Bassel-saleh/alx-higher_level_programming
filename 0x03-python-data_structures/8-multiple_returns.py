#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == 0:
        c_tuple = (None)
        return c_tuple
    else:
        c_tuple = (len(sentence), sentence[0])
        return c_tuple

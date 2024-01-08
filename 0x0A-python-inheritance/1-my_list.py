#!/usr/bin/python3
''' Module for my list class '''


class MyList(list):
    '''subclass MyList'''
    def print_sorted(self):
        print(sorted(self))

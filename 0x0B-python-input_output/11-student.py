#!/usr/bin/python3
''' defining to_json function '''


class Student:
    ''' defines a student '''
    def __init__(self, first_name, last_name, age):
        ''' initializes student '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        ''' etrieves a dictionary representation of a Student
        instance (same as 8-class_to_json.py): '''
        try:
            for attr in attrs:
                if type(attr) is not str:
                    return self.__dict__
        except Exception:
            return self.__dict__
        c_dict = dict()
        for key, value in self.__dict__.items():
            if key in attrs:
                c_dict[key] = value
        return c_dict
    def reload_from_json(self, json):
        ''' replaces all attributes of the Student instance '''
        for key, value in json.items():
            if key in self.__dict__:
                self.__dict__[key] = value

#!/usr/bin/python3
""" Class to json """


def class_to_json(obj):
    """returns the dictionary description with simple
    data structure same as self.__dict__
    """
    return vars(obj)

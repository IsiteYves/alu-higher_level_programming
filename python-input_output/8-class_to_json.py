#!/usr/bin/python3
"""Returns the dictionary description for JSON serialization of an object"""


def class_to_json(obj):
    """Returns the dictionary representation of an obj"""
    return obj.__dict__

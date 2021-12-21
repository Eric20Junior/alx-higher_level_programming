#!/usr/bin/python3
"""
Module 3-to_json_string.py

A function that returns the JSON representation of an object (string)
"""

def to_json_string(my_obj):
    """Return a string"""
    import json

    return json.dumps(my_obj)

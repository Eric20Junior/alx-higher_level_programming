#!/usr/bin/python3
"""Module 4-from_json_string.py

Write a function that returns an object (Python data structure) represented by aJSON string
"""

def from_json_string(my_str):
    """Return a python data struction as a JSON string"""
    import json

    return json.loads(my_str)

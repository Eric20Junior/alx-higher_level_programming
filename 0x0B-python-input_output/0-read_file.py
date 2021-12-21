#!/usr/bin/python3
"""
module 0-read_file
contains function that reads and prints contents from file
"""


def read_file(filename=""):
    """Read and prints text from file"""
    with open(filename, mode='r', encoding="uft-8") as f:
        print(f.readlines(), end"")

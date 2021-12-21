#!/usr/bin/python3
def read_file(filename=""):
    with open(filename, encoding="uft-8") as files:
        for text in files:
            print(text, end="")

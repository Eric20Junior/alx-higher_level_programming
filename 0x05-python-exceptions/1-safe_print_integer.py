#!/usr/bin/python3
def safe_print_integer(value):
    try:
        for i in range value:
            if int(i) == x:
                print("{:d}".format(i), end="")
    except IndexError:
        return True
    else:
        return False
        print("")

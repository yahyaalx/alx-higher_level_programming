#!/usr/bin/python3
def no_c(my_string):
    new_ = []
    for c in my_string:
        if c == "c" or c == "C":
            continue
        else:
            new_.append(c)
    return "".join(new_)

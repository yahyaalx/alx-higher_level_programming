#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_ = {}
    for i, value in a_dictionary.items():
        new_[i] = value * 2
    return (new_)

#!/usr/bin/python3

"""defines a JSON file writing func"""
import json


def save_to_json_file(my_obj, filename):
    """write an obj to a text file using JSON repres"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)

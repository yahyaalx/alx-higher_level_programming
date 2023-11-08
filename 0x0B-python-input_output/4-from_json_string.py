#!/usr/bin/python3

"""defines a JSON to object func"""
import json


def from_json_string(my_str):
    """return the python obj repres of a JSON string"""
    return json.loads(my_str)

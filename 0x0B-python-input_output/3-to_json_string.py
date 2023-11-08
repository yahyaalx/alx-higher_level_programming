#!/usr/bin/python3

"""defines a string to JSON func"""
import json


def to_json_string(my_obj):
    """return the JSON repres of a string obj"""
    return json.dumps(my_obj)

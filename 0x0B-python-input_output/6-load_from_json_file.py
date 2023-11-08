#!/usr/bin/python3
"""defines a JSON file reading func"""
import json


def load_from_json_file(filename):
    """create a python obj from a JSON file"""
    with open(filename) as f:
        return json.load(f)

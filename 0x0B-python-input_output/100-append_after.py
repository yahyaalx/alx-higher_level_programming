#!/usr/bin/python3
"""def a func to insert text into a file"""

def append_after(filename="", search_string="", new_string=""):
    """insert text after each line containing a specific string in a file"""
    file_content = ""
    with open(filename) as file_to_read:
        for line_in_file in file_to_read:
            file_content += line_in_file
            if search_string in line_in_file:
                file_content += new_string
    with open(filename, "w") as file_to_write:
        file_to_write.write(file_content)

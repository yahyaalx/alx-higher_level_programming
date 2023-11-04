#!/usr/bin/python3
"""
This module, "5-test_indentation", contains a function to format text.

"""

def text_indentation(text):
    """Formats a text by inserting line breaks after certain punctuation marks.
    
    Args:
        text: The text to be formatted.
        
    Raises:
        TypeError: If the input is not a string.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    
    flag = 0
    for char in text:
        if flag == 0 and char == ' ':
            continue
        else:
            flag = 1
        
        if flag == 1:
            print(char, end="")
            if char in ['?', '.', ':']:
                print("\n")
                flag = 0

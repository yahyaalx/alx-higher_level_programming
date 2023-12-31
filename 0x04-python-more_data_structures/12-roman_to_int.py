#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str:
        return 0

    roman_to_int = {"I": 1, "V": 5, "X": 10, "L": 50,\
         "C": 100, "D": 500, "M": 1000}
    total = 0
    i = 0

    while i < len(roman_string):
        if (
            i + 1 < len(roman_string)
            and roman_to_int[roman_string[i]]\
                 < roman_to_int[roman_string[i + 1]]
        ):
            total += roman_to_int[roman_string[i + 1]]\
                 - roman_to_int[roman_string[i]]
            i += 2
        else:
            total += roman_to_int[roman_string[i]]
            i += 1
    return int(total)
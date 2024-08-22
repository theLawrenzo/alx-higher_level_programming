#!/usr/bin/python3
def roman_to_int(roman_string):
    if not type(roman_string) is str or roman_string is None:
        return 0

    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50,\
            'C': 100, 'D': 500, 'M': 1000}

    length = len(roman_string)
    val = 0
    i = 0

    while i < length:
        if i == length-1:
            val += roman_numerals[roman_string[i]]
            return val

        first = roman_numerals[roman_string[i]]
        second = roman_numerals[roman_string[i+1]]
        
        if first < second:
            val -= first
        else:
            val += first

        i += 1

    return val

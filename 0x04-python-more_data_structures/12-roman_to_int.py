#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_numerals = {'I': 1, 'II': 2, 'III': 3, 'V': 5, 'X': 10,\
            'L': 50, 'C': 100, 'D': 500, 'M': 1000}


if __name__ == '__main__':
    roman_to_int(6)

#!/usr/bin/python3
def remove_char_at(str, n):
    i = 0
    new_str = ''
    for c in str:
        if i == n:
            continue
        new_str = new_str + c
        i += 1

    return new_str

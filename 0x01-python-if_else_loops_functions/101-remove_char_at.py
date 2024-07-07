#!/usr/bin/python3
def remove_char_at(str, n):
    i = 0
    new_str = ''
    str_len = len(str)

    while i < str_len:
        if i == n:
            i += 1
            continue
        new_str = new_str + str[i]
        i += 1

    return new_str

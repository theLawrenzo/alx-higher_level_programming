#!/usr/bin/python3
'''
Appends a string to the end of a text file and returns the number
of characters read

The file is created if it doesn't exist.
'''
def append_write(filename="", text=""):
    with open(filename, 'a', encoding="utf-8") as f:
        add = f.append(text)

    return add
if __name__ == '__main__':
    import doctest
    doctest.testmod()

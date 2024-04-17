#!/usr/bin/python3
def write_file(filename="", text=""):
    '''
    Writes a string to a text file

    Returns: The number of characters written
    '''
    with open(filename, 'w', encoding="utf-8") as f:
        written = f.write(text)

    return written

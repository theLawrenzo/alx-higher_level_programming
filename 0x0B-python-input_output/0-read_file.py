#!/usr/bin/python3
def read_file(filename=""):
    '''
        Reads text from a file and prints to standard output
    '''
    with open(filename, 'r', encoding="utf-8") as f:
        text = f.read()

    print(text, end='')
    return None

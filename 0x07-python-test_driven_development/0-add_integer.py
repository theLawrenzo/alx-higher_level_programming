#!/usr/bin/python3
'''
    Adds two integers and Return the value from the addition

    Args:
        a - first value, should be an integer or a float
        b - second value, should be an integer or a float

    Return:
        a + b

    Raises:
        TypeError: If a is not in ['int', 'float']
        TypeError: If b is not in ['int', 'float']

    >>> add_integer(1, 2)
    3
    >>> add_integer('a', 2)
    Traceback (most recent last call):
        ...
    TypeError: a must be an integer
    >>> add_integer(1, 'b')
    Traceback (most recent last call):
        ...
    TypeEror: b must be an integer
'''
def add_integer(a, b):
    if isinstance(a, str) == 'True':
        raise TypeError ('a must be an integer')
    if isinstance(a, bool) == 'True':
        raise TypeError ('a must be an integer')
    if isinstance(b, str) == 'True':
        raise TypeError ('b must be an integer')
    if isinstance(b, bool) == 'True':
        raise TypeError ('b must be an integer')

    if isinstance(a, float):
        a = int(a)

    if isinstance(b, float):
        b = int(b)

    return a + b

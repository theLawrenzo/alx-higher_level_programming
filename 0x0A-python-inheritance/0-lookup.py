#!/usr/bin/python3
""" Returns a list of available attributes and methods of an object """

def lookup(obj):
    return [x for x in dir(obj)]

#!/usr/bin/python3
class Base:
    '''Manages id attribute in all my future classes'''
    __nb_objects = 0
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            __nb_objects += 1
            id = __nb_objects

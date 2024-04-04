#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        i = 0
        while i < x:
            print('{:d}'.format(my_list[i], end=''))
            i = i+1
        print()

    except ValueError:
        pass

    except IndexError:
        print('{:d}'.format(my_list[i]))

    return i

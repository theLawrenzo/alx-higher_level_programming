#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    while True:
        try:
            for i in my_list:
                print("{}".format(i), end="")
                i += 1

        except Exception:
            print('An error occured!')
    return i

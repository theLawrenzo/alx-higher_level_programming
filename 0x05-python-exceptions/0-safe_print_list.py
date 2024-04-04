#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    while True:
        try:
            cnt = 0
            for i in my_list:
                print("{}".format(i), end="")
                cnt += 1
            return cnt

        except IndexError:
            return cnt

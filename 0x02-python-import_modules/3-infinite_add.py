#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    num = len(sys.argv) - 1
    arg = 0
    if num == 1:
        print(sys.argv[1])
    elif num > 1:
        i = 1
        while i <= num:
            arg += int(sys.argv[i])
            i += 1
    print(arg)

#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    num = len(sys.argv) - 1
    if num == 0:
        print(f"{num} arguments.")
    elif num == 1:
        print(f"{num} argument:")
        print(f"{num}: {sys.argv[num]}")
    elif num > 1:
        print(f"{num} arguments:")
        i = 1
        while i <= num:
            print(f"{i}: {sys.argv[i]}")
            i += 1

#!/usr/bin/python3
import sys
for i in argv:
    if len(argv) == 0:
        print("0 arguments.")
    else:
        print("{:d} arguments:".format(len(argv)))
        print("{:d}: {:s}".format(count, i))
        count = count + 1
if __name__ == "__main__":
    import sys

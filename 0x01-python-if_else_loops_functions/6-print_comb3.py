#!/usr/bin/python3
i = 0
while i < 10:
    j = 0
    while j < 10:
        if i == j or i >  j:
            j = j + 1
            continue
        if i == 8 and j == 9:
            print("{:d}{:d}".format(i, j))
        else:
            print("{:d}{:d},".format(i, j), end=" ")
        j = j + 1
    i = i + 1

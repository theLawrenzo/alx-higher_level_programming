#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last = abs(number) % 10
    last = -last
else:
    last = number % 10

if last > 5:
    print(f"Last digit of {number} is {last} and is greater than {5}")
elif last == 0:
    print(f"Last digit of {number} is {last} and is {number}")
elif last < 6 and last != 0:
    print(f"Last digit of {number} is {last} and is less than {6} and not {0}")

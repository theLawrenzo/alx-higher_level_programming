#!/usr/bin/python3
import sys
import calculator_1

if __name__ == '__main__':
    length = len(sys.argv)
    if length < 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])

    if sys.argv[2] == '+':
        c = calculator_1.add(a, b)
        print('{0} + {1} = {2}'.format(a, b, c))
    elif sys.argv[2] == '-':
        c = calculator_1.sub(a, b)
        print('{0} - {1} = {2}'.format(a, b, c))
    elif sys.argv[2] == '*':
        c = calculator_1.mul(a, b)
        print('{0} * {1} = {2}'.format(a, b, c))
    elif sys.argv[2] == '/':
        c = calculator_1.div(a, b)
        print('{0} / {1} = {2}'.format(a, b, c))
    else:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)

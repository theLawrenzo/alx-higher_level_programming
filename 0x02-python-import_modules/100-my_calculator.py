#!/usr/bin/python3
import calculator_1 as calculators

calcs = [arg for arg in calculators if not arg.startswith('__')]
print(calcs)

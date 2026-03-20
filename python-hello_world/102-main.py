#!/usr/bin/python3
# We use __import__ because the filename starts with a number
magic_calculation = __import__("102-magic_calculation").magic_calculation

a = 2
b = 3
print("Result: {}".format(magic_calculation(a, b)))

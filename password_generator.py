#!/usr/bin/python3
"""
Author: Chris Martinez
Date: 26 Fe 2023
Version: 1.0
Description: Quick Random Password Generator
"""

import random

is_integer = False
chars = 'abcdefghijklmnopqrstuvwxyz1234567890!?.,-'
password = ""

length = input("Enter the desire length for your new password: ")
while (is_integer == False):
    try:
        length.strip()
        length = int(length)
        if (length <= 0):
            raise ValueError
    except ValueError as err:
        print("Invalid input, you must enter a positive integer.")
        length = input("Please enter desired length of password: ")
    else:
        is_integer = True


for c in range(length):
    password += random.choice(chars)

print(password)


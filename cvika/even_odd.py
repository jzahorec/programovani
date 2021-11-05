# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 22:53:09 2021

@author: jzahorec

Even and Odd
"""

import sys

numbers = sys.stdin.read()

number_str = ""
odd = list()
separators = [" ", "\n"]

# print(numbers)

for char in numbers:
    if char == "-":  # ze zadani dat vyplyva, ze po - musi nasledovat 1 tudiz -1
        break
    if (char in separators) and (len(number_str) > 0):
        number = int(number_str)
        number_str = ""
        if number % 2 == 0:
            print(number, end=" ")
        else:
            odd.append(number)
    else:
        number_str += char

for num in odd:
    print(num, end=" ")

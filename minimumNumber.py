#!/bin/python3

import math
import os
import random
import re
import sys

"""
Its length is at least 6.
It contains at least one digit.
It contains at least one lowercase English character.
It contains at least one uppercase English character.
It contains at least one special character. The special characters are: !@#$%^&*()-+
"""

# Complete the minimumNumber function below.
def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    
    special_chars = '!@#$%^&*()-+'

    has_digit = any(map(lambda x: x.isdigit(), password))
    has_lc = any(map(lambda x: x.islower(), password))
    has_uc = any(map(lambda x: x.isupper(), password))
    has_special = any(map(lambda x: x in special_chars, password))

    to_add = 4-sum([has_digit, has_lc, has_uc, has_special])

    if to_add < (6-n):
        to_add = (6-n)
    
    return to_add


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()

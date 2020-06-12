#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations

# Complete the alternate function below.
def alternate(s):

    # 1. get the combinations, s=#unique chars - 2
    # 2. iterrate each combinations
    # 3. deleting characters from string of each iterrate item
    # 4. check the resultant length == 1
    # 5. if 4 is met, count the length of the new string
    # 6. register the longest length so far
    # 7. return the longest length

    longest = 0
    if len(s) > 1 and len(set(s))>1: # if s is like 'a' or 'aaaa', skip below process
        n = len(set(s))-2 # the letters to be removed

        for item in combinations(set(s), n):
            reduced_s = (s+'.')[:-1] #create an independent copy

            for letter in item:
                reduced_s = reduced_s.replace(letter, '')

            if (len(set(reduced_s[::2]))==1) and (len(set(reduced_s[1::2]))==1):
                longest = max(longest, len(reduced_s))
    
    return longest


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()

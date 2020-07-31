#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the anagram function below.
#https://www.hackerrank.com/challenges/anagram/problem
def anagram(s):
    if len(s)%2:
        return -1
    else:
        size = len(s)
        a, b = Counter(s[:size//2]), Counter(s[size//2:])
        y = sum((a-b).values())
        if y:
            return y
        else:
            return 0



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()

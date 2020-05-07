#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the fairRations function below.
def fairRations(B):
    n = len(B)
    breads = 0

    for pos, val in enumerate(B):
        if val%2 and pos <= (n-2):
            breads += 2
            B[pos+1] += 1
    if B[-1]%2: #if the last value after operation becomes odd
        return 'NO'
    else:
        return breads

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    N = int(input())

    B = list(map(int, input().rstrip().split()))

    result = fairRations(B)

    fptr.write(str(result) + '\n')

    fptr.close()

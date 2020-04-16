#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cutTheSticks function below.
def cutTheSticks(arr):
    arr = sorted(arr, reverse=True)
    n = [len(arr)]

    while arr:
        min_val = min(arr)        
        min_index = arr.index(min_val)
        arr = arr[:min_index]
        n.append(len(arr))
    
    return n[:-1]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

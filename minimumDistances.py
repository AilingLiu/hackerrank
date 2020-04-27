#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumDistances function below.
def minimumDistances(a):
    uniques = set(a)
    n=len(a)
    min_d = float('inf')

    for val in uniques:
        l,r = a.index(val), n-1-a[::-1].index(val)

        if r != l:
            d =  (r-l)
            min_d = min(min_d, d)

    #return the min distance
    if min_d == float('inf'):
        return -1
    else:
        return min_d


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()

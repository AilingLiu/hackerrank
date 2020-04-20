#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):

    jump = 0
    current = 0
    n = len(c)-1

    while current < n:
        # always consider two units of jump first, if c[current_position + 2 units] doesn't hit a bump (i.e.: cloud 1)
        if ((current + 2) <= n) and (c[current + 2] != 1):
            current += 2
        else:
            current += 1
        jump += 1
    return jump


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()

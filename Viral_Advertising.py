#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.
def viralAdvertising(n):

    cumulative = 2
    liked = 2

    for day in range(1, n+1):
        if day == 1:
            pass
        else:
            liked = (liked*3)//2
            cumulative += liked

    return cumulative

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()

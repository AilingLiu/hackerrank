#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the gameOfThrones function below.
#https://www.hackerrank.com/challenges/game-of-thrones/problem
def gameOfThrones(s):
    #if odd length:
    ## the matched word would be having 1 odd count

    # if even length
    ## every matched word counts are even

    n = len(s)
    counts = Counter(s)
    n_odd = sum(x%2 != 0 for x in counts.values())
    if n%2:
        if n_odd==1:
            return 'YES'
        else:
            return 'NO'
    else:
        if n_odd== 0:
            return 'YES'
        else:
            return 'NO'



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()

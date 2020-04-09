#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):

    init_pos = 0
    jump = 0
    thunder = 0
    n = len(c)

    while (init_pos != 0) or (jump == 0):
        init_pos =  (init_pos + k)%n
        jump += 1
        if c[init_pos]==1:
            thunder += 1        

    return 100-(jump*1 + thunder*2)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()

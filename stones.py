#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the stones function below.

def stones(n, a, b):

    """
    a	b	c			#1	#0	#total
    0	0	0			0	3	30
    0	0	1			1	2	120
    0	1	0			1	2	120
    1	0	0			1	2	120
    0	1	1			2	1	210
    1	0	1			2	1	210
    1	1	0			2	1	210
    1	1	1			3	0	300
    """

    ans = set()
    for i in range(n):
        ans.add((n-1-i)*a + i*b)

    return sorted(ans)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input())

    for T_itr in range(T):
        n = int(input())

        a = int(input())

        b = int(input())

        result = stones(n, a, b)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()

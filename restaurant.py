#!/bin/python3

import os
import sys

#
# https://www.hackerrank.com/challenges/restaurant/problem
#
def restaurant(l, b):
    #
    # Write your code here.
    #
    r = min(l, b)
    common_div = max(m for m in range(1, r+1) if l%m==0 and b%m==0)
    return l*b//pow(common_div, 2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        lb = input().split()

        l = int(lb[0])

        b = int(lb[1])

        result = restaurant(l, b)

        fptr.write(str(result) + '\n')

    fptr.close()

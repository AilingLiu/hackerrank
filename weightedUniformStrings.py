#!/bin/python3

import math
import os
import random
import re
import sys

# https://www.hackerrank.com/challenges/weighted-uniform-string/problem
def weightedUniformStrings(s, queries):
    
    # get a list of weights from uniform string
      # para: weights, uniform string
      # uniform string

    # loop over the queries, return Yes or No

    weights_arr = set()
    weight = 0
    prev = s[0]
    for c in s:
        if c==prev:
            weight+=(ord(c)-ord('a')+1)
        else:
            prev=c
            weight=(ord(c)-ord('a')+1)
        weights_arr.add(weight)
    
    res = []
    for q in queries:
        if q in weights_arr:
            res.append('Yes')
        else:
            res.append('No')
    return res



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()

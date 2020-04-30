#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the workbook function below.
def workbook(n, k, arr):
    
    # loop over arr list, each element represent num of problems (arr[i]) in each chapter
    # how many pages for each arr[i] problem/chapter
    # what are the page number for each chapter
    # does the page number equal the problem number on it
    # if yes, special num + 1
    # return total number of special number

    start = 1
    special = 0

    for num_prob in arr:
        pages = math.ceil(num_prob/ k) # how many pages in this chapter
        pages_num = list(range(start, start+pages)) #e.g. [1,2] 2 pages

        prob_n = list(range(1, 1+num_prob)) # e.g. [1,2,3,4] 4 problems

        for i, val in enumerate(pages_num): # first 1(index 0) from [1,2], then 2(index 1) from [1, 2]
            if val in prob_n[i*k:((i+1)*k)]: # index*k:(index+1)*k or index*k:(index*k+k)
                special += 1
        start += pages
    return special


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()

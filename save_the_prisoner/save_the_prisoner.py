#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the saveThePrisoner function below.
def saveThePrisoner(n, m, s):
    """
    n : the number of prisoners
    m : the number of sweets
    s : the chair number to start passing out treats at
    """
    # candy number is smaller than prisoners
    if m <= n:
        poison = s+m-1

    else:
        prev_p = s-1
        if prev_p == 0:
            prev_p = n
        poison = prev_p + (m%n)

    return poison


if __name__ == '__main__':
    f = open('test_cases.txt', 'r')
    t = int(f.readline())

    for t_itr in range(t):
        nms = f.readline().split()

        n = int(nms[0])

        m = int(nms[1])

        s = int(nms[2])

        result = saveThePrisoner(n, m, s)
        print(result)


    f.close()

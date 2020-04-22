#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kaprekarNumbers function below.

splitN = lambda x: list(map(int, list(str(x))))
getNum = lambda arr: int(''.join(map(str, arr)))

def checkNum(val):

    d = len(splitN(val))
    power2 = splitN(val**2)
    #print('power2 list: ', power2)

    if len(power2)==1:
        newV = power2[0]

    else:
        ind = len(power2)-d
        l, r = getNum(power2[:ind]), getNum(power2[ind:])
        #print('left: ', l)
        #print('right: ', r)
        newV = l+r

    if newV==val:
        return val

def kaprekarNumbers(p, q):
    klist = []

    for val in range(p, q+1):
        #print('\nVerify: ', val)
        if checkNum(val):
            #print('It is kaprekar num.')
            klist.append(val)
        #else:
            #print('Not kaprekar Num.')

    if klist:
        print(*klist)
    else:
        print('INVALID RANGE')


if __name__ == '__main__':
    p = int(input())

    q = int(input())

    kaprekarNumbers(p, q)

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the saveThePrisoner function below.
def saveThePrisoner(n, m, s):
    return (m%n)+(s-1)


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

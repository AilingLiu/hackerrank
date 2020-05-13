#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the happyLadybugs function below.
def happyLadybugs(b):


    if '_' in b:

        for letter in b:
            if letter != '_':
                if b.count(letter)<2:
                    return 'NO'
    else:

        for i, letter in enumerate(b):
            if b.count(letter)<2:

                return 'NO'
            else:
                if i>=1 and i<(len(b)-1):

                    if (b[i]!=b[i-1]) and (b[i]!=b[i+1]):

                        return 'NO'

    return 'YES'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input())

    for g_itr in range(g):
        n = int(input())

        b = input()

        result = happyLadybugs(b)

        fptr.write(result + '\n')

    fptr.close()

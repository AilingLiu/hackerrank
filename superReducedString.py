#!/bin/python3

import math
import os
import random
import re
import sys
import collections


def superReducedString(s):
    
    list_s = list(s)
    i = 0


    # When there is nothing to reduce, the i reach to the end of the string, hence break the loop
    while i<len(list_s)-1: 
        if list_s[i] == list_s[i+1]:
        # find the repeated letter and delete them from the list
            list_s.pop(i)
            list_s.pop(i)
            i=0 #after the string is reduced, i has to start over with 0 index
        else:
            i+=1
    

    if list_s:
        return ''.join(list_s)

    else:
        return 'Empty String'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()

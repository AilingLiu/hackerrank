#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the makingAnagrams function below.
def makingAnagrams(s1, s2):
    
    #num of letter in each string
    #minus the difference
    s1_dict = {x: s1.count(x) for x in set(s1)}
    s2_dict = {x: s2.count(x) for x in set(s2)}
    
    n_delete = 0

    #common keys
    common_key = set(s1_dict).intersection(set(s2_dict))
    for l in common_key:
        n_delete+= abs(s1_dict[l]-s2_dict[l])

    #non-common keys
    non_common = set(s1_dict).symmetric_difference(set(s2_dict))
    for l in non_common:
        if l in s1_dict:
            n_delete += s1_dict[l]
        elif l in s2_dict:
            n_delete += s2_dict[l]
    
    return n_delete
    



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = makingAnagrams(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()

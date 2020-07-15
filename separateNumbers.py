#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the separateNumbers function below.
def separateNumbers(s):
    #not beautiful simple cases: starts by 0, or single digit

    #if not the above condition, check below condition, example: 99100101
     # 1.get the first digit: s[0]=9
     # 2.create new string by incrementing 1 until length is equal to len(s)
     # 3.evaluate whether s is in the new string
     # 4. if not, get the first two digit, repeat 2 to 4
     # loop until len(first_digit) == half size of len(s)
     
    n = len(s) #s=99100101, n=8
    if n <=1 or s.startswith('0'): #fail: 09100101, or 1
        print('NO')
    else:
        l = 1 #initiate number of digit
        while True:
            if l <= n//2: #loop over n digit
                first = s[:l] #s[:1]-->9
                l+=1 #prepare for next n digit: l-->2
                i=1
                k=l
                new_s = first #news--> 9
                while k <= n: #k=1
                    next_val = int(first)+i #next value: 10 
                    i += 1
                    k += len(str(next_val)) # k=3
                    new_s += str(next_val) #news: 910
                if s==new_s:
                    print(f'YES {first}')
                    break
            else:
                print('NO')
                break


if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)

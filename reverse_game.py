#!/bin/python3

import math
import os
import random
import re
import sys

#https://www.hackerrank.com/challenges/reverse-game/problem
def get_kval(n, k):
    #example n = 5, odd number
    #final list: [4,0,3,1,2]
    #consisted of 2 lists: [4, 3], [0, 1, 2] in alternative combination

    #example n = 6, even number
    #final list: [5, 0, 4, 1, 3, 2]
    #consisted of 2 lists: [5, 4, 3], [0, 1, 2] in alternative combination
    
    #generalize rule for values in 2 sub lists:
    # for odd n: list1= [n-1, n-2, ... n//2], list2=[0, 1, ... n//2+1] *
    # for even n: list1 = [n-1, n-2, ... n//2-1], list2=[0, 1, ...n//2] *
    # * in range function, the last value is not included
    
    #to find k from list 1 and list 2:
    # final list: [4, 0, 3, 1, 2]
    # list1=[4, 3], list2=[0,1,2], corresponding i of final list: [0, 2], [1,3,4]
    # let k = 3, let m = list1.index(k), then i=2m
    # let k = 1, let j = list2.index(k), then i=2j+1
    # let k = 2, if k equals to the last value of list2, then i=n-1

    if n%2: 
        l1=range(n-1, (n//2), -1)
        l2=range(0, n//2+1)
    else: #nb is even
        l1=range(n-1, (n//2)-1, -1)
        l2 = range(0, (n//2)) 

    if k in l1:
        return l1.index(k)*2
    else:
        if k==l2[-1]:
            return n-1
        else:
            return l2.index(k)*2+1

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])
        print(get_kval(n, k))
        

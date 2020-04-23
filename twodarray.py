
import math
import os
import random
import re
import sys


# Complete the beautifulTriplets function below.
def beautifulTriplets(d, arr):

    cnt = 0
    for i, numi in enumerate(arr[:-2], start=0):
        for j, numj in enumerate(arr[i+1:], start=i+1):
            if numj - numi == d:
                for numk in arr[j+1:]:
                    if numk - numj == d:
                        cnt +=1
    return cnt


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    arr = list(map(int, input().rstrip().split()))

    result = beautifulTriplets(d, arr)

    fptr.write(str(result) + '\n')

    fptr.close()

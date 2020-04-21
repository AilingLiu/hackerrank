#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the acmTeam function below.
def acmTeam(topic):

    max_top = 0
    pairs = 0

    n = len(topic)
    for i in range(n):
        for j in range(i+1, n):
            bin_code = bin(int(topic[i], 2) | int(topic[j], 2))
            cnt = bin_code.count('1')
            if cnt > max_top:
                max_top = cnt
                pairs = 1
            elif cnt == max_top:
                pairs += 1
    return max_top, pairs


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

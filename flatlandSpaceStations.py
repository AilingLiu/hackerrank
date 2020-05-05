#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the flatlandSpaceStations function below.

diff = lambda arr: [arr[i+1] - arr[i] for i in range(len(arr)-1)]

def flatlandSpaceStations(n, c):

    """
    Take the concept of mario jumping game.
    
    Each station is the stone where Mario can rest,
    starting from 0, finishing at n-1 (0-index). The difference is:
    those stones also has a number on it representing the distance from starting point.
    
    so c = [0, 4] means the first stone is 0km from city 0, and second second stone is 4km from city 0.
    
    We want to find out which two stones have the miximum distance,
    representing which two stations have the largest distance.
    
    if the maximum distance is at either end of the journey, then return the maximum distance.
    if not, then divide the distance by 2, and get the floor value. The metohpor for this method is:
    imagine there is a very long crew of business men traveling across desert with camels. There are cities behind 
    and also in front of the crew. The city has water.
    So now, which unlucky person in the crew has the furthest distance from the water? The middle one!
    And how far? The length of the crew/2!
   
    """

    c.extend([0, n-1])

    c_sorted=sorted(c)

    c_df = diff(c_sorted)

    max_dis = max(c_df)

    max_diss = max(math.floor(max_dis/2), c_df[-1], c_df[0])

    return max_diss


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = flatlandSpaceStations(n, c)

    fptr.write(str(result) + '\n')

    fptr.close()

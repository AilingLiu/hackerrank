#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cavityMap function below.
def cavityMap(grid):

    n = len(grid)
    #not check: row 0, column 0, row (n-1), column (n-1) -- step 1

    #change the string in to list format
    grid = [list(string) for string in grid]

    #to check: the remains: row[1:-1], col[1:-1] -- step 2
    for i in range(1, n-1):
        for j in range(1, n-1):
            #current index: i, j
            curr = grid[i][j]
            #print(curr)
            #top index: i-1, j
            top = grid[i-1][j]
            #bottom index: i+1, j
            bottom = grid[i+1][j]
            #left index: i, j-1
            left = grid[i][j-1]
            #right index: i, j+1
            right = grid[i][j+1]
            #if the values in all these four index are smaller than value at [i][j]
            if curr > top and curr > bottom and curr > left and curr > right:
                #change current value to 'X'
                grid[i][j] = 'X'
    
    grid = [''.join(r) for r in grid]
    return grid



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)


    result = cavityMap(grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()

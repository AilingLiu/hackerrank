#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the dayOfProgrammer function below.
def is_leap_year(year):
    if year <= 1917: #julian
        return year%4==0
    else: #Gregorian 
        return ((year%400==0) or (year%4==0 and year%100!=0))

def dayOfProgrammer(year):

    if is_leap_year(year):
        return '12.09.{}'.format(year)

    else:

        if year == 1918:
            return '26.09.{}'.format(year) 

        else:
            return '13.09.{}'.format(year)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()

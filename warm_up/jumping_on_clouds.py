#!/bin/python3
#https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem
#engrjepmanzanillo

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    i = 0
    jump_index = [0]
    while i <= len(c) - 2:
        try:
            if c[i+2] == 0:
                jump_index.append(i+2)
                i += 2
            elif c[i+1] == 0:
                jump_index.append(i+1)
                i += 1
        except:
            if c[i+1] == 0:
                jump_index.append(i+1)
                i += 1
    
    return len(jump_index) - 1


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #n = int(input())

    #c = list(map(int, input().rstrip().split()))
    c = [0,1,0,0,0,1,0]
    #c = [0,0,0,1,0,0]
    #c = [0,1,0,0,1,0]
    #result = jumpingOnClouds(c)
    print(jumpingOnClouds(c))

    #fptr.write(str(result) + '\n')

    #fptr.close()

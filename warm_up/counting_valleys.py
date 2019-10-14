#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    steps = [item for item in s]
    #convert steps into numerical values, U=+1, D=-1
    steps = [1 if step=='U' else -1 for step in steps]
    steps.insert(0,0)
    total = 0
    steps_num = [] #cummulative sum to get relative position from sea level
    for step in steps:
      total = total + step
      steps_num.append(total)
    valley_count = 0 #valley count
    #valley count will trigger if cummulative sum is -1 followed by 0
    for i in range(1, len(steps_num)):
      if steps_num[i] == 0 and steps_num[i-1] == -1:
        valley_count += 1
    print(valley_count)

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #n = int(input())
    n = 8
    #s = input()
    s = 'UDDDUDUU'

    countingValleys(n, s)

    #fptr.write(str(result) + '\n')

    #fptr.close()

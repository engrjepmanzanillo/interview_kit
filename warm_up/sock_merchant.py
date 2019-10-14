#!/bin/python3
#https://www.hackerrank.com/challenges/sock-merchant/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
#engrjepmanzanillo

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    complete_socks = []
    for item in ar:
        if item not in complete_socks:
            complete_socks.append(item)
    pair_count = []
    for sock in complete_socks:
        pair_count.append(ar.count(sock) // 2)
    return sum(pair_count)

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = 9

    #ar = list(map(int, input().rstrip().split()))
    ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
    print(sockMerchant(n, ar))

    #fptr.write(str(result) + '\n')

    #fptr.close()
#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'fizzBuzz' function below.
#
# The function accepts INTEGER n as parameter.
#

def printAns(W, L):
    # Write your code here
    counter = 0
    target = set(W)
    word_list = set('0')
    for l in L:
        if l not in word_list:
            word_list.add(l)
            if target == set(l):
                counter += 1
    print(counter)
        
if __name__ == '__main__':
    W = input().rstrip()
    L = list(map(str, input().rstrip().split()))
    printAns(W, L)
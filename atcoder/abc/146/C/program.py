import sys
input = sys.stdin.readline
import math
import numpy as np

def check(m,x,a, b):
    return x >= a * m + b * len(str(m))
def print_ans(A, B, X):
    """Test Case
    >>> print_ans(10, 7, 100)
    9
    >>> print_ans(2, 1, 100000000000)
    1000000000
    >>> print_ans(1000000000, 1000000000, 100)
    0
    >>> print_ans(1234, 56789, 314159265)
    254309
    """
    left = 0
    right = 10 ** 9 + 1
    while  right - left > 1:
        mid = (right + left) // 2
        if check(mid, X, A, B):
            left = mid
        else:
            right = mid
    print(left)

if __name__ == '__main__':
    A, B, X = map(int, input().rstrip().split())
    print_ans(A, B, X)

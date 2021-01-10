import numpy as np
import sys

from numpy.core.fromnumeric import argmax
input = sys.stdin.readline


def print_ans(N, A):
    """Test Case
    >>> print_ans(2, "1 4 2 5")
    2
    >>> print_ans(2,"3 1 5 4")
    1
    >>> print_ans(4, "6 13 12 5 3 7 10 11 16 9 8 15 2 1 14 4")
    2
    """
    ar = np.array(list(map(int, A.rstrip().split())))
    left = ar[:2 ** (N-1)]
    right = ar[2 ** (N-1):]
    left_max = np.argmax(left)
    right_max = np.argmax(right)
    # print(left)
    # print(right)
    if left[left_max] > right[right_max]:
        print(right_max+1 + 2**(N-1))
    else:
        print(left_max+1)


if __name__ == '__main__':
    N = int(input().rstrip())
    A = input()
    print_ans(N, A)

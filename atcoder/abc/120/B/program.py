import sys
input = sys.stdin.readline
import numpy as np
def print_ans(A, B, K):
    """Test Case
    >>> print_ans(8, 12, 2)
    2
    >>> print_ans(100, 50, 4)
    5
    >>> print_ans(1, 1, 1)
    1
    """
    counter = 0
    for i in range(1, min(A, B) + 1)[::-1]:
        if A % i == 0 and B % i == 0:
            counter += 1
        if counter == K:
            print(i)
            break


if __name__ == '__main__':
    A, B, K = map(int, input().rstrip().split())
    print_ans(A, B, K)

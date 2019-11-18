import sys
input = sys.stdin.readline
import numpy as np
def print_ans(N, L):
    """Test Case
    >>> print_ans(5, 2)
    18
    >>> print_ans(3, -1)
    0
    >>> print_ans(30, -50)
    -1044
    """
    ar = np.arange(N)
    ar = ar + L
    minimum = np.argmin(np.abs(ar))
    print(np.sum(ar) - ar[minimum])



if __name__ == '__main__':
    N, L = map(int, input().rstrip().split())
    print_ans(N, L)



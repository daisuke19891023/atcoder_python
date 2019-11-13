import sys
input = sys.stdin.readline
import numpy as np
def print_ans(N, ar):
    """Test Case
    >>> print_ans(3, [1, 4, 3])
    4
    3
    4
    >>> print_ans(2, [5, 5])
    5
    5
    """
    ar = np.array(ar)
    ar_idx = np.argsort(ar)

    for i in range(N):
        for k in reversed(range(N)):
            if i != ar_idx[k]:
                print(ar[ar_idx[k]])
                break

if __name__ == '__main__':
    N = int(input().rstrip())
    ar = [int(input().rstrip()) for i in range(N)]
    print_ans(N, ar)

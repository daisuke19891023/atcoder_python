from numba import njit
import numpy as np
import sys
input = sys.stdin.readline


@njit
def print_ans(N, K, pr, cr):
    """Test Case
    >>> print_ans(5, 3,[2, 4, 5, 1, 3], [3, 4, -10, -8, 8])
    8
    >>> print_ans(2, 3,[2, 1],[10, -7])
    13
    """
    maximum = 0
    pr = np.array(pr)
    pr = pr - 1
    cr = np.array(cr)
    maximum = max(maximum, np.max(cr))
    ar = cr.copy()
    for i in range(K):
        if len(ar.shape) == 1:
            newest = ar.copy()
        else:
            newest = ar[i, :].copy()
        tmp = newest[pr]
        ar = np.vstack((ar, tmp))
        tmp_sum = np.sum(ar, axis=0)
        maximum = max(maximum, np.max(tmp_sum))
    print(maximum)


if __name__ == '__main__':
    N, K = map(int, input().rstrip().split())
    pr = list(map(int, input().rstrip().split()))
    cr = list(map(int, input().rstrip().split()))
    print_ans(N, K, pr, cr)

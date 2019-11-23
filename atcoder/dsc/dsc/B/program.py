import sys
input = sys.stdin.readline
import numpy as np
def print_ans(N, ar):
    """Test Case
    >>> print_ans(3, [2, 4, 3])
    3
    >>> print_ans(12, [100, 104, 102, 105, 103, 103, 101, 105, 104, 102, 104, 101])
    0
    """
    ar = np.array(ar)
    sum_ar = np.sum(ar)
    br = np.add.accumulate(ar)
    cr = br - sum_ar / 2
    dr = abs(cr)
    # er = np.where(dr == dr.min())
    er = np.argmin(dr)
    if dr[er] == 0:
        print("0")
    else:
        left = np.sum(ar[:er + 1])
        right = np.sum(ar[er + 1:])
        print(abs(left - right))

if __name__ == '__main__':
    N = int(input().rstrip())
    ar = list(map(int, input().rstrip().split()))
    print_ans(N, ar)



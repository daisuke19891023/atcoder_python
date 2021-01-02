import re
import sys
import numpy as np
import copy
from collections import deque
input = sys.stdin.readline
np.set_printoptions(precision=9)


def print_ans(N, ar):
    """Test Case
    >>> print_ans(5,[7.5,2.4,17.000000001,17,16.000000000])
    3
    >>> print_ans(11,[0.9,1,1,1.25,2.30000,5,70,0.000000001,9999.999999999,0.999999999,1.000000001])
    8
    """
    ar = deque(ar)
    array = deque()
    array.append(np.array(ar, dtype='float64'))
    for i in range(N-1):
        tmp = ar.popleft()
        ar.append(tmp)
        array.append(np.array(ar, dtype='float64'))
    array = np.array(array)
    ans = 0
    for i in range(N-1):
        a1 = array[i, 0] * (10 ** 9)
        a2 = array[i, 1:N-i] * (10 ** 9)
        tmp_list = a1 * a2
        ans += np.count_nonzero(tmps != 10 ** 18)
    print(ans)


if __name__ == '__main__':
    N = int(input().rstrip())
    ar = [float(input().rstrip()) for _ in range(N)]
    print_ans(N, ar)

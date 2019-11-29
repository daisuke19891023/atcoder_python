import sys
input = sys.stdin.readline
import numpy as np
import math
def print_ans(ar):
    """Test Case
    >>> print_ans(['29', '20', '7', '35','120'])
    215
    >>> print_ans(['101', '86', '119','108', '57'])
    481
    >>> print_ans(['123', '123', '123','123','123'])
    643
    """
    tmp_list = np.array([int(a[-1]) for a in ar])
    tmp_list[tmp_list == 0] = 10
    min_arg = tmp_list.argmin()
    ans = 0
    for i, a in enumerate(ar):
        if i != min_arg:
            tmp = math.ceil(int(a) / 10) * 10
        else:
            tmp = int(a)
        ans += tmp
    print(ans)


    

if __name__ == '__main__':
    ar = [input().rstrip() for _ in range(5)]
    print_ans(ar)

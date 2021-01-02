import sys
input = sys.stdin.readline
import math
import numpy as np

def print_ans(N, xr):
    """Test Case
    >>> print_ans(3, [[[2, 1]], [[1, 1]], [[2, 0]]])
    2
    """
    ans_list = [[-1] * N ] * N
    print(ans_list)
    for i, x in enumerate(xr):
        print(x)
        for a in x:
            print(a,ans_list[i][a[0] -1],a[1])
            ans_list[i][a[0] -1] = a[1]
            print(ans_list)
    print(ans_list)


if __name__ == '__main__':
    N = int(input().rstrip())
    xr = []
    for _ in range(N):
        ar = []
        A = int(input().rstrip())
        for _ in range(A):    
            ar.append(list(map(int, input().rstrip().split())))
        xr.append(ar)
    print_ans(N, xr)

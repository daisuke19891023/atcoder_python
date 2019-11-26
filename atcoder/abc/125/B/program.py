import sys
input = sys.stdin.readline
import numpy as np
def print_ans(N, vs, cs):
    """Test Case
    >>> print_ans(3, [10, 2, 5], [6, 3, 4])
    5
    >>> print_ans(4,[13, 21, 6, 19], [11, 30, 6, 15])
    6
    >>> print_ans(1,[1],[50])
    0
    """
    vs = np.array(vs)
    cs = np.array(cs)
    tmps = vs - cs
    ans_list = tmps[tmps > 0]
    if len(ans_list) == 0:
        print("0")
    else:
        print(np.sum(ans_list))
if __name__ == '__main__':
    N = int(input().rstrip())
    vs = list(map(int, input().rstrip().split()))
    cs = list(map(int, input().rstrip().split()))
    print_ans(N, vs, cs)

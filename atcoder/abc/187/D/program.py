import numpy as np
import sys
input = sys.stdin.readline


def print_ans(N, lr):
    """Test Case
    >>> print_ans(4,[[2, 1],[2, 2],[5, 1],[1, 3]])
    1
    """
    np_L = np.array(lr)
    np_L_T = np_L.T
    A = np_L_T[0]
    B = np_L_T[1]
    X = -np.sum(A)
    C = 2 * A + B
    C = list(np.sort(C))
    ans = 0
    while X <= 0:
        X += C.pop()
        ans += 1
    print(ans)


if __name__ == '__main__':
    N = int(input().rstrip())
    L = [list(map(int, input().split())) for i in range(N)]
    print_ans(N, L)

import sys
input = sys.stdin.readline
import numpy as np
def print_ans(N, M, C, br, ar):
    """Test Case
    >>> print_ans(2, 3, -10, [1, 2, 3], [[3, 2, 1], [1, 2, 2]])
    1
    >>> print_ans(5, 2, -4, [-2, 5], [[100, 41], [100, 40], [-3, 0], [-6, -2], [18, -13]])
    2
    >>> print_ans(3, 3, 0, [100, -100, 0], [[0, 100, 100], [100, 100, 100], [-100, 100, 100]])
    0
    """
    br = np.array(br)
    ans = 0
    for a in ar:
        tmp = np.dot(np.array(a), br)
        if tmp + C > 0:
            ans+= 1
    print(ans)

if __name__ == '__main__':
    N, M, C = map(int, input().rstrip().split())
    br = list(map(int, input().rstrip().split()))
    ar = [list(map(int, input().rstrip().split())) for _ in range(N)]
    print_ans(N, M, C, br, ar)

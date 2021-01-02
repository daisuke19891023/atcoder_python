import sys
input = sys.stdin.readline
from decimal import Decimal,ROUND_HALF_UP
def print_ans(N, M, ar):
    """Test Case
    >>> print_ans(3, 4,[[2, 1, 3],[3, 1, 2, 3], [2, 3, 2]])
    1
    >>> print_ans(5, 5,[[4, 2, 3, 4, 5],[4, 1, 3, 4, 5],[4, 1, 2, 4, 5],[4, 1, 2, 3, 5],[4, 1, 2, 3, 4]])
    0
    """
    base = [i for i in range[M]]
    ans = []
    for a in ar:
        


if __name__ == '__main__':
    N, M = map(int, input().rstrip().split())
    ar = [input().rstrip().split() for _ in range(N)]
    print_ans(N, M, ar)

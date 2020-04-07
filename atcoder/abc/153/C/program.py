import sys
input = sys.stdin.readline
import math
def print_ans(N, K, ar):
    """Test Case
    >>> print_ans(3, 1, [4, 1, 5])
    5
    >>> print_ans(8, 9, [7, 9, 3, 2, 3, 8, 4, 6])
    0
    >>> print_ans(3, 0, [1000000000, 1000000000, 1000000000])
    3000000000
    """
    if K >= len(ar):
        print(0)
    elif K == 0:
        print(sum(ar))
    else:
        ar = sorted(ar)
        print(sum(ar[:-K]))

if __name__ == '__main__':
    N, K = map(int, input().rstrip().split())
    ar = list(map(int,input().rstrip().split()))
    print_ans(N, K, ar)



import sys
input = sys.stdin.readline
import numpy as np
def print_ans(N, ar):
    """Test Case
    >>> print_ans(5, [2, 6, 1, 4, 5])
    YES
    >>> print_ans(6, [4, 1, 3, 1, 6, 2])
    NO
    >>> print_ans(2, [10000000, 10000000])
    NO
    """
    br = set(ar)
    print("YES" if len(br) == N else "NO")
    

if __name__ == '__main__':
    N = int(input().rstrip())
    ar = list(map(int,input().rstrip().split()))
    print_ans(N, ar)



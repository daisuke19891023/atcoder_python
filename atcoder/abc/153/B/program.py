import sys
input = sys.stdin.readline
import math
def print_ans(H, N, ar):
    """Test Case
    >>> print_ans(10, 3, [4, 5, 6])
    Yes
    >>> print_ans(20, 3, [4, 5, 6])
    No
    >>> print_ans(210, 5, [31, 41, 59, 26, 53])
    Yes
    >>> print_ans(211, 5, [31, 41, 59, 26, 53])
    No
    """
    if H <= sum(ar):
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    H, N = map(int, input().rstrip().split())
    ar = list(map(int,input().rstrip().split()))
    print_ans(H, N, ar)



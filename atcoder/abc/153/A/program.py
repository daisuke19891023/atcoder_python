import sys
input = sys.stdin.readline
import math
def print_ans(H, A):
    """Test Case
    >>> print_ans(10, 4)
    3
    >>> print_ans(1, 10000)
    1
    >>> print_ans(10000, 1)
    10000
    """
    print(math.ceil(H / A))


if __name__ == '__main__':
    H, A = map(int, input().rstrip().split())
    print_ans(H, A)



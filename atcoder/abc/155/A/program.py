import sys
input = sys.stdin.readline
import math
def print_ans(ar):
    """Test Case
    >>> print_ans([5, 7, 5])
    Yes
    >>> print_ans([4, 4, 4])
    No
    >>> print_ans([4, 9, 6])
    No
    >>> print_ans([3, 3, 4])
    Yes
    """
    print("Yes" if len(set(ar)) == 2 else "No")


if __name__ == '__main__':
    ar = list(map(int, input().rstrip().split()))
    print_ans(ar)



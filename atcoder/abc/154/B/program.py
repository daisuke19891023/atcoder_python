import sys
input = sys.stdin.readline
import math
def print_ans(S):
    """Test Case
    >>> print_ans("sardine")
    xxxxxxx
    >>> print_ans("xxxx")
    xxxx
    >>> print_ans("gone")
    xxxx
    """
    print("x" * len(S))


if __name__ == '__main__':
    S = input().rstrip()
    print_ans(S)



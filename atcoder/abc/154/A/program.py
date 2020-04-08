import sys
input = sys.stdin.readline
import math
def print_ans(S, T, A, B, U):
    """Test Case
    >>> print_ans("red", "blue", 3, 4, "red")
    2 4
    >>> print_ans("red", "blue", 5, 5, "blue")
    5 4
    """
    if S == U:
        A = A -1
    else:
        B = B -1
    print('{} {}'.format(A, B))


if __name__ == '__main__':
    S, T = input().rstrip().split()
    A, B = map(int, input().rstrip().split())
    U = input().rstrip()
    print_ans(S, T, A, B, U)



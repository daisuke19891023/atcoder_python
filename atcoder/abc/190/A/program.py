import sys
input = sys.stdin.readline


def print_ans(A, B, C):
    """Test Case
    >>> print_ans(2, 1, 0)
    Takahashi
    >>> print_ans(2, 2, 0)
    Aoki
    >>> print_ans(2, 2, 1)
    Takahashi
    """
    if A > B:
        print("Takahashi")
    elif B > A:
        print("Aoki")
    elif C == 0:
        print("Aoki")
    else:
        print("Takahashi")


if __name__ == '__main__':
    A, B, C = map(int, input().rstrip().split())
    print_ans(A, B, C)

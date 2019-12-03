import sys
input = sys.stdin.readline
def print_ans(A, B, C):
    """Test Case
    >>> print_ans(2, 11, 4)
    4
    >>> print_ans(3, 9, 5)
    3
    >>> print_ans(100, 1, 10)
    0
    """
    print(min(C, B // A))


if __name__ == '__main__':
    A, B, C = map(int, input().rstrip().split())
    print_ans(A, B, C)



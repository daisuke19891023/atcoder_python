import sys
input = sys.stdin.readline
def print_ans(A, P):
    """Test Case
    >>> print_ans(1, 3)
    3
    >>> print_ans(0, 1)
    0
    >>> print_ans(32, 21)
    58
    """
    print((A * 3 + P) // 2)

if __name__ == '__main__':
    A, P= map(int, input().rstrip().split())
    print_ans(A, P)



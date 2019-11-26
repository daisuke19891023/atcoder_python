import sys
input = sys.stdin.readline
def print_ans(A, B, T):
    """Test Case
    >>> print_ans(3, 5, 7)
    10
    >>> print_ans(3, 2, 9)
    6
    >>> print_ans(20, 20, 19)
    0
    """
    tmp, _ = divmod(T, A)
    print(tmp * B)

if __name__ == '__main__':
    A, B, T = map(int, input().rstrip().split())
    print_ans(A, B, T)



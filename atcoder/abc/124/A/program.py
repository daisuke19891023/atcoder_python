import sys
input = sys.stdin.readline
def print_ans(A, B):
    """Test Case
    >>> print_ans(5, 3)
    9
    >>> print_ans(3, 4)
    7
    >>> print_ans(6, 6)
    12
    """
    ans = sorted([A, B, A - 1, B - 1])
    print(ans[-1] + ans[-2])

if __name__ == '__main__':
    A, B = map(int, input().rstrip().split())
    print_ans(A, B)



import sys
input = sys.stdin.readline
def print_ans(N, A, B):
    """Test Case
    >>> print_ans(4, 2, 9)
    8
    >>> print_ans(4, 2, 7)
    7
    >>> print_ans(4, 2, 8)
    8
    """
    print(min(N * A, B))

if __name__ == '__main__':
    N, A, B = map(int, input().rstrip().split())
    print_ans(N, A, B)

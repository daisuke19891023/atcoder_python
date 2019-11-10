import sys
input = sys.stdin.readline
def print_ans(A, B):
    """Test Case
    >>> print_ans(-13, 3)
    -10
    >>> print_ans(1, -33)
    34
    >>> print_ans(13, 3)
    39
    """
    print(max(max(A + B, A - B), A * B))

if __name__ == '__main__':
    A, B = map(int,input().rstrip().split())
    print_ans(A, B)

import sys
input = sys.stdin.readline
def print_ans(A, B, C):
    """Test Case
    >>> print_ans(6, 4, 3)
    1
    >>> print_ans(8, 3, 9)
    4
    >>> print_ans(12, 3, 7)
    0
    """
    print(max(0,C - A + B))

if __name__ == '__main__':
    A, B, C = map(int,input().rstrip().split())
    print_ans(A, B, C)

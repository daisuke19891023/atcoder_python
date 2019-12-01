import sys
input = sys.stdin.readline
import math
tax = 1.08
def print_ans(N):
    """Test Case
    >>> print_ans(432)
    400
    >>> print_ans(1079)
    :(
    >>> print_ans(1001)
    927
    """
    X = int(N // tax)
    if N == math.floor(X * tax):
        print(X)
    elif N == math.floor((X + 1) * tax):
        print(X + 1)
    else:
        print(":(")
    
if __name__ == '__main__':
    N = int(input().rstrip())
    print_ans(N)

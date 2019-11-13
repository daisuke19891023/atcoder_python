import sys
input = sys.stdin.readline
import math
def print_ans(N, D):
    """Test Case
    >>> print_ans(6, 2)
    2
    >>> print_ans(14, 3)
    2
    >>> print_ans(20, 4)
    3
    """
    print(math.ceil(N / (D * 2 + 1)))
    

if __name__ == '__main__':
    N, D = map(int,input().rstrip().split())
    print_ans(N, D)

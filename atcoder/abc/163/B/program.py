import sys
input = sys.stdin.readline
def print_ans(N, M, ar):
    """Test Case
    >>> print_ans(41, 2, [5, 6])
    30
    >>> print_ans(10, 2, [5, 6])
    -1
    >>> print_ans(11, 2, [5, 6])
    0
    """
    tmp = N -sum(ar)
    if(tmp >= 0):
        print(tmp)
    else:
        print("-1")



if __name__ == '__main__':
    N, M = map(int, input().rstrip().split())
    ar = list(map(int, input().rstrip().split()))
    print_ans(N, M, ar)



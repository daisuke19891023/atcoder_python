import sys
input = sys.stdin.readline
def print_ans(N):
    """Test Case
    >>> print_ans(4)
    1
    >>> print_ans(999999)
    499999
    """
    q, mod = divmod(N,2)
    if(mod == 0):
        print(q - 1)
    else:
        print(q)

if __name__ == '__main__':
    N = int(input().rstrip())
    print_ans(N)

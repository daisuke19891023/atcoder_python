import sys
input = sys.stdin.readline
def print_ans(S, W):
    """Test Case
    >>> print_ans(4, 5)
    unsafe
    >>> print_ans(100, 2)
    safe
    >>> print_ans(10, 10)
    unsafe
    """
    if S > W :
         print('safe')
    else:
        print('unsafe')
if __name__ == '__main__':
    S, W = map(int, input().rstrip().split())
    print_ans(S, W)


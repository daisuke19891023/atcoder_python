import sys
input = sys.stdin.readline
def print_ans(r):
    """Test Case
    >>> print_ans(4)
    48
    >>> print_ans(15)
    675
    >>> print_ans(80)
    19200
    """
    print(3 * (r ** 2))

if __name__ == '__main__':
    r = int(input().rstrip())
    print_ans(r)

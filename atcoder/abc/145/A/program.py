import sys
input = sys.stdin.readline
def print_ans(r):
    """Test Case
    >>> print_ans(2)
    4
    >>> print_ans(100)
    10000
    """
    print(r ** 2)

if __name__ == '__main__':
    r = int(input().rstrip())
    print_ans(r)



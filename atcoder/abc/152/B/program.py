import sys
input = sys.stdin.readline
def print_ans(a, b):
    """Test Case
    >>> print_ans(4, 3)
    3333
    >>> print_ans(7, 7)
    7777777
    """
    if a > b:
        print(str(b) * a)
    else:
        print(str(a) * b)


if __name__ == '__main__':
    a, b = map(int, input().rstrip().split())
    print_ans(a, b)



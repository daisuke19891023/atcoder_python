import sys
input = sys.stdin.readline
def print_ans(input_line):
    """Test Case
    >>> print_ans(2)
    8
    >>> print_ans(1)
    1
    """
    print(str(input_line ** 3))

if __name__ == '__main__':
    s = int(input().rstrip())
    print_ans(s)
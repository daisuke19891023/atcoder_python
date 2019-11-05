import sys
input = sys.stdin.readline
def print_ans(input_line):
    """Test Case
    >>> print_ans(4)
    0.5
    >>> print_ans(5)
    0.6
    >>> print_ans(1)
    1.0
    """
    q, mod = divmod(input_line,2)
    print((q + mod)/input_line)

if __name__ == '__main__':
    print_ans(int(input()))
import sys
input = sys.stdin.readline
import math
def print_ans(input_line):
    """Test Case
    >>> print_ans("4 10")
    3
    >>> print_ans("8 9")
    2
    >>> print_ans("8 8")
    1
    """
    A, B = map(int,input_line.split())
    print(math.ceil((B-1)/(A-1)))

if __name__ == '__main__':
    s = input().rstrip()
    print_ans(s)
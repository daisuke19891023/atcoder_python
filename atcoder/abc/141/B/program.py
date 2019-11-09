import sys
input = sys.stdin.readline
import re
def print_ans(input_line):
    """Test Case
    >>> print_ans("RUDLUDR")
    Yes
    >>> print_ans("DULL")
    No
    >>> print_ans("UUUUUUUUUUUUUUU")
    Yes
    >>> print_ans("ULURU")
    No
    >>> print_ans("RDULULDURURLRDULRLR")
    Yes
    """
    odd = input_line[::2]
    even = input_line[1::2]
    if re.search(r'L', odd) == None and re.search(r'R',even) == None:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    s = input().rstrip()
    print_ans(s)
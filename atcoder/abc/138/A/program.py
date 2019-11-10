import sys
input = sys.stdin.readline
def print_ans(a,s):
    """Test Case
    >>> print_ans(3200,"pink")
    pink
    >>> print_ans(3199,"pink")
    red
    >>> print_ans(4049, "red")
    red
    """
    if a >= 3200:
        print(s)
    else:
        print("red")


if __name__ == '__main__':
    a = int(input().rstrip())
    s = input().rstrip()
    print_ans(a,s)

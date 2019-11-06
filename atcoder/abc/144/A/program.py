import sys
input = sys.stdin.readline
def print_ans(input_line):
    """Test Case
    >>> print_ans("2 5")
    10
    >>> print_ans("5 10")
    -1
    >>> print_ans("9 9")
    81
    """
    A,B = input_line.split()
    if len(A) == 1 and len(B) == 1:
        print(int(A) * int(B))
    else:
        print("-1")


if __name__ == '__main__':
    print_ans(input())

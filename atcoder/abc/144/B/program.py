import sys
input = sys.stdin.readline
def print_ans(input_line):
    """Test Case
    >>> print_ans("10")
    Yes
    >>> print_ans("50")
    No
    >>> print_ans("81")
    Yes
    """
    N = int(input_line)
    for i in range(1,10):
        q, mod= divmod(N,i)
        if mod == 0 and 0 < q < 10:
            print("Yes")
            break
        elif i == 9:
            print("No")


if __name__ == '__main__':
    print_ans(input())

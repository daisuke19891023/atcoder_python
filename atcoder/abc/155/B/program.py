import sys
input = sys.stdin.readline
def print_ans(N, ar):
    """Test Case
    >>> print_ans(5, [6, 7, 9, 10, 31])
    APPROVED
    >>> print_ans(3, [28, 27, 24])
    DENIED
    """
    flg = True
    for a in ar:
        if a % 2 == 0 and a % 3 != 0 and a % 5 != 0:
            flg = False
            break

    if flg:
        print("APPROVED")
    else:
        print("DENIED")



if __name__ == '__main__':
    N = int(input().rstrip())
    ar = list(map(int, input().rstrip().split()))
    print_ans(N, ar)



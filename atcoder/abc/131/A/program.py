import sys
input = sys.stdin.readline
def print_ans(S):
    """Test Case
    >>> print_ans("3776")
    Bad
    >>> print_ans("8080")
    Good
    >>> print_ans("1333")
    Bad
    >>> print_ans("0024")
    Bad
    """
    flg = True
    tmp = ""
    for s in S:
        if tmp == s:
            flg = False
            break
        tmp = s
    if flg:
        print("Good")
    else:
        print("Bad")



if __name__ == '__main__':
    S = input().rstrip()
    print_ans(S)



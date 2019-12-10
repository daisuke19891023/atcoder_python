import sys
input = sys.stdin.readline

def print_ans(S):
    """Test Case
    >>> print_ans("2019/04/30")
    Heisei
    >>> print_ans("2019/11/01")
    TBD
    """
    S = int("".join(S.split("/")))
    if S <= 20190430:
        print("Heisei")
    else:
        print("TBD")


if __name__ == '__main__':
    S = input().rstrip()
    print_ans(S)



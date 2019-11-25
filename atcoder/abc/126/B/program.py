import sys
input = sys.stdin.readline
def print_ans(S):
    """Test Case
    >>> print_ans("1905")
    YYMM
    >>> print_ans("0112")
    AMBIGUOUS
    >>> print_ans("1700")
    NA
    """
    front = int(S[:2])
    rear = int(S[2:])
    frontMM_flg = 1 <= front <= 12
    rearMM_flg = 1 <= rear <= 12
    if frontMM_flg and rearMM_flg:
        print("AMBIGUOUS")
    elif frontMM_flg and not rearMM_flg:
        print("MMYY")
    elif not frontMM_flg and rearMM_flg:
        print("YYMM")
    else:
        print("NA")
    


if __name__ == '__main__':
    S = input().rstrip()
    print_ans(S)

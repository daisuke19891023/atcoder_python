import sys
input = sys.stdin.readline
def print_ans(S):
    """Test Case
    >>> print_ans("ASSA")
    Yes
    >>> print_ans("STOP")
    No
    >>> print_ans("FFEE")
    Yes
    """
    ans_arr = []
    ans_arr.append(S[0])


    for s_ch in S[1:]:
        for a_ch in ans_arr:
            if s_ch != a_ch:
                ans_arr.append(s_ch)
    if len(set(ans_arr)) == 2:
        print("Yes")
    else:
        print("No")



if __name__ == '__main__':
    S = input().rstrip()
    print_ans(S)



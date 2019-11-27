import sys
input = sys.stdin.readline
def print_ans(S):
    """Test Case
    >>> print_ans("000")
    1
    >>> print_ans("10010010")
    3
    >>> print_ans("0")
    0
    """
    before = "2"
    ans = 0
    for s in S:
        if s == before:
            ans += 1
            if s == "1":
                before = "0"
            else:
                before = "1"
        else:
            before = s

    print(ans)

if __name__ == '__main__':
    S = input().rstrip()
    print_ans(S)

import sys
input = sys.stdin.readline
def print_ans(S, T):
    """Test Case
    >>> print_ans("CSS", "CSR")
    2
    >>> print_ans("SSR","SSR")
    3
    """
    ans = 0
    for i in range(len(S)):
        if S[i] == T[i]:
            ans += 1
    print(ans)


if __name__ == '__main__':
    S = input().rstrip()
    T = input().rstrip()
    print_ans(S, T)
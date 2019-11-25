import sys
input = sys.stdin.readline
def print_ans(N, K, S):
    """Test Case
    >>> print_ans(3, 1, "ABC")
    aBC
    >>> print_ans(4, 3, "CABA")
    CAbA
    """
    tmp = S[K - 1].lower()
    ans = [tmp if i == K - 1 else s for i, s in enumerate(S) ]
    print(''.join(ans))

if __name__ == '__main__':
    N, K = map(int, input().rstrip().split())
    S = input().rstrip()
    print_ans(N, K, S)



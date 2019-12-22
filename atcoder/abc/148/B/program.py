import sys
input = sys.stdin.readline

def print_ans(N, S, T):
    """Test Case
    >>> print_ans(2, "ip", "cc")
    icpc
    >>> print_ans(8, "hmhmnknk", "uuuuuuuu")
    humuhumunukunuku
    >>> print_ans(5, "aaaaa", "aaaaa")
    aaaaaaaaaa
    """
    ans = []
    for i in range(N):
        ans.append(S[i])
        ans.append(T[i])
    print(''.join(ans))

if __name__ == '__main__':
    N = int(input().rstrip())
    S, T = input().rstrip().split()
    print_ans(N, S, T)



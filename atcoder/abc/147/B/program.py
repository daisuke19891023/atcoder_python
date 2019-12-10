import sys
input = sys.stdin.readline

def print_ans(N):
    """Test Case
    >>> print_ans("redcoder")
    1
    >>> print_ans("vvvvvv")
    0
    >>> print_ans("abcdabc")
    2
    """
    ans = 0
    length = len(N)
    for i in range(length // 2):
        if N[i] != N[length -1 - i]:
            ans += 1
    print(ans)

    

if __name__ == '__main__':
    N = input().rstrip()
    print_ans(N)



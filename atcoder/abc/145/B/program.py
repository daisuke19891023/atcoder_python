import sys
input = sys.stdin.readline
def print_ans(N, S):
    """Test Case
    >>> print_ans(6, "abcabc")
    Yes
    >>> print_ans(6, "abcadc")
    No
    >>> print_ans(1, "z")
    No
    """
    if N % 2 != 0:
        print("No")
    else:
        if S[:N//2] == S[N//2:]:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    N = int(input().rstrip())
    S = input().rstrip()
    print_ans(N, S)

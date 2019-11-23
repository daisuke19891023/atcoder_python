import sys
input = sys.stdin.readline
def print_ans(A, B):
    """Test Case
    >>> print_ans(30, 100)
    100
    >>> print_ans(12, 100)
    50
    >>> print_ans(0, 100)
    0
    """
    if A > 12:
        ans = B
    elif 6 <= A <= 12:
        ans = B // 2
    else:
        ans = 0
    print(ans)

if __name__ == '__main__':
    A, B = map(int, input().rstrip().split())
    print_ans(A, B)



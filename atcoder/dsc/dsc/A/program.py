import sys
input = sys.stdin.readline
def print_ans(A, B):
    """Test Case
    >>> print_ans(1, 1)
    1000000
    >>> print_ans(3, 101)
    100000
    >>> print_ans(4, 4)
    0
    """
    ans = 0
    if A == 1:
        ans += 300000
    elif A == 2:
        ans += 200000
    elif A == 3:
        ans += 100000

    if B == 1:
        ans += 300000
    elif B == 2:
        ans += 200000
    elif B == 3:
        ans += 100000

    if A == 1 and B == 1:
        ans += 400000
    print(ans)

if __name__ == '__main__':
    A, B = map(int, input().rstrip().split())
    print_ans(A, B)



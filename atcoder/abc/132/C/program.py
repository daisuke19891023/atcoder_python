import sys
input = sys.stdin.readline
def print_ans(n,dr):
    """Test Case
    >>> print_ans(6, [9, 1, 4, 4, 6, 7])
    2
    >>> print_ans(8, [9, 1, 14, 5, 5, 4, 4, 14])
    0

    >>> print_ans(14, [99592, 10342, 29105, 78532, 83018, 11639, 92015, 77204, 30914, 21912, 34519, 80835, 100000, 1])
    42685
    """
    ans_ar = sorted(dr)
    print(ans_ar[n//2] - ans_ar[n//2 - 1])

if __name__ == '__main__':
    n = int(input().rstrip())
    dr = list(map(int, input().rstrip().split()))
    print_ans(n,dr)



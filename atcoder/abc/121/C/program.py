import sys
input = sys.stdin.readline
def print_ans(N, M, arr):
    """Test Case
    >>> print_ans(2, 5, [[4, 9], [2, 4]])
    12
    >>> print_ans(4, 30, [[6, 18], [2, 5], [3, 10], [7, 9]])
    130
    >>> print_ans(1, 100000,[[1000000000, 100000]])
    100000000000000
    """
    ans = 0
    tmp = M
    arr = sorted(arr)
    for ar in arr:
        if tmp > ar[1]:
            ans += ar[0] * ar[1]
        else:
            ans += ar[0] * tmp
            break
        tmp -= ar[1]
    print(ans)


if __name__ == '__main__':
    N, M = map(int, input().rstrip().split())
    arr = [list(map(int, input().rstrip().split())) for _ in range(N)]
    print_ans(N, M, arr)

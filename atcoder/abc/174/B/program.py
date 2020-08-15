import sys
input = sys.stdin.readline


def print_ans(D, ar):
    """Test Case
    >>> print_ans(5, [[0, 5],[-2, 4], [3, 4],[4, -4]])
    3
    >>> print_ans(3, [[1, 1], [1, 1], [1, 1], [1, 1], [1, 2], [1, 3], [2, 1], [2, 2], [2, 3], [3, 1], [3, 2], [3, 3]])
    7
    """
    ans = 0
    X = D ** 2
    for a in ar:
        if a[0] ** 2 + a[1] ** 2 <= X:
            ans += 1
    print(ans)


if __name__ == '__main__':
    N, D = map(int, input().rstrip().split())
    ar = [list(map(int, input().rstrip().split())) for _ in range(N)]
    print_ans(D, ar)

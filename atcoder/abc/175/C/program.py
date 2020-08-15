import sys
input = sys.stdin.readline


def print_ans(X, K, D):
    """Test Case
    >>> print_ans(6, 2, 4)
    2
    >>> print_ans(7, 4, 3)
    1
    >>> print_ans(10, 1, 2)
    8
    >>> print_ans(1000000000000000,1000000000000000,1000000000000000)
    1000000000000000
    """
    # 移動しない
    if K % 2 == 0 and D >= abs(X):
        print(abs(X))
    elif K % 2 != 0 and D >= abs(X):
        print(min(abs(X-D), abs(X+D)))
    elif abs(X) - D * K >= 0:
        print(abs(abs(X) - D * K))
    else:
        # near 0
        tmp, _ = divmod(abs(X), D)
        rest_K = K - tmp
        a = abs(abs(X) - tmp * D)
        b = abs(abs(X) - (tmp + 1) * D)
        if rest_K % 2 == 0:
            print(a)
        else:
            print(b)


if __name__ == '__main__':
    X, K, D = map(int, input().rstrip().split())
    print_ans(X, K, D)

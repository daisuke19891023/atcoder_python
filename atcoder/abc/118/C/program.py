import sys
input = sys.stdin.readline
import re
def print_ans(N, ar, lr):
    """Test Case
    >>> print_ans(5, [100, 90, 80], [98, 40, 30, 21, 80])
    23
    >>> print_ans(8, [100, 90, 80], [100, 100, 90, 90, 90, 80, 80, 80])
    0
    >>> print_ans(8, [1000, 800, 100], [300, 333, 400, 444, 500, 555, 600,666])
    243
    """
    lr = sorted(lr)[::-1]
    ans = 0
    # unchange
    del_list = []
    for i, a in enumerate(ar):
        for j, l in enumerate(lr):
            if a == l:
                del_list.append([i, j])
                break
    for a in del_list[::-1]:
        del ar[a[0]]
        del lr[a[1]]
    print(ar, lr)

        


if __name__ == '__main__':
    N, *ar = map(int, input().rstrip().split())
    lr = [int(input().rstrip()) for _ in range(N)]
    print_ans(N, ar, lr)

import sys
input = sys.stdin.readline


def print_ans(N, C, L):
    """Test Case
    >>> print_ans(2, 6,[[1, 2, 4],[2, 2, 4]])
    10
    """
    ans_list = []
    for l in L:
        ans_list.append((l[0]-1, l[2]))
        ans_list.append((l[1], -l[2]))
    ans_list.sort()

    ans = 0
    fee = 0
    t = 0
    for x, y in ans_list:
        if x != t:
            ans += min(C, fee) * (x-t)
            t = x
        fee += y

    print(ans)


if __name__ == '__main__':
    N, C = map(int, input().split())
    L = [list(map(int, input().split())) for i in range(N)]
    print_ans(N, C, L)

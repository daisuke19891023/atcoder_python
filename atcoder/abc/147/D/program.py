import sys
input = sys.stdin.readline
def print_ans(N, ar):
    """Test Case
    >>> print_ans(3, [1, 2, 3])
    6
    >>> print_ans(10, [3, 1, 4, 1, 5, 9, 2, 6, 5, 3])
    237
    >>> print_ans(10, [3, 14, 159, 2653, 58979, 323846, 2643383, 27950288, 419716939, 9375105820])
    103715602
    """
    ans_list = [0] * N
    ans_list[N-1] = ar[N-1]
    for i in range(len(ar) - 1)[::-1]:
        for a in ar[i+1:]
            tmp ^= a
        ans_list[i] = tmp
    print(sum(ans_list) % (10 ** 9 + 7))
    # ans = 0
    # for i in range(N -1):
    #     for k in range(i, N):
    #         ans += ar[i] ^ ar[k]
    # print(ans % (10 ** 9 + 7))

if __name__ == '__main__':
    N = int(input().rstrip())
    ar = list(map(int, input().rstrip().split()))
    print_ans(N, ar)

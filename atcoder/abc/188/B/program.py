import sys
input = sys.stdin.readline


def print_ans(N, A, B):
    """Test Case
    >>> print_ans(2, [-3, 6], [4, 2])
    Yes
    >>> print_ans(2, [4, 5],[-1, -3])
    No
    >>> print_ans(3,[1, 3, 5], [3, -6, 3])
    Yes
    """
    ans = 0
    for i in range(N):
        tmp = A[i] * B[i]
        ans += tmp
    if ans == 0:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    N = int(input().rstrip())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    print_ans(N, A, B)

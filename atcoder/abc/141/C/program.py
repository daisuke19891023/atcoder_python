import sys
input = sys.stdin.readline
def print_ans(N, K, Q, arr):
    """Test Case
    >>> print_ans(6, 3, 4, [3, 1, 3, 2])
    No
    No
    Yes
    No
    No
    No
    >>> print_ans(6, 5, 4, [3, 1, 3, 2])
    Yes
    Yes
    Yes
    Yes
    Yes
    Yes
    >>> print_ans(10, 13, 15,[3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9])
    No
    No
    No
    No
    Yes
    No
    No
    No
    Yes
    No
    """
    point = [K - Q] * N
    for a in arr:
        point[a - 1] += 1
    ans_arr = ["Yes" if p > 0 else "No" for p in point]
    for ans in ans_arr:
        print(ans)

if __name__ == '__main__':
    N, K, Q = map(int,input().rstrip().split())
    arr = [ int(input()) for i in range(Q)]
    print_ans(N, K, Q, arr)
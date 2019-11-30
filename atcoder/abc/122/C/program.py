import sys
input = sys.stdin.readline
def print_ans(N, Q, S, arr):
    """Test Case
    >>> print_ans(8, 3, "ACACTACG", [[3, 7], [2, 3], [1, 8]])
    2
    0
    3
    """
    t = [0] * (N+1)
    for i in range(N):
        t[i+1] = t[i] + (1 if S[i:i+2] == "AC" else 0)
    for ar in arr:
        print(t[ar[1] - 1] - t[ar[0] - 1] )

if __name__ == '__main__':
    N, Q = map(int, input().rstrip().split())
    S = input().rstrip()
    arr = [list(map(int, input().rstrip().split())) for _ in range(Q)]
    print_ans(N, Q, S, arr)

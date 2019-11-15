import sys
input = sys.stdin.readline
def print_ans(N, A):
    """Test Case
    >>> print_ans(3, [2, 2, 4])
    4 0 4
    >>> print_ans(5, [3, 8, 7, 5, 5])
    2 4 12 2 8
    >>> print_ans(3, [1000000000, 1000000000, 0])
    0 2000000000 0
    """
    # x0 = S - (a2 + a4 + ...)
    S = sum(A)
    xr = [0] * N
    xr[0] = S - 2 * (sum(A[1::2]))
    for i in range(1,N):
        xr[i] = 2 * A[i-1] - xr[i-1] 
    print(" ".join(list(map(str, xr))))

if __name__ == '__main__':
    N =  int(input().rstrip())
    A= list(map(int, input().rstrip().split()))
    print_ans(N, A)

import sys
input = sys.stdin.readline
def print_ans(N, input_line):
    """Test Case
    >>> print_ans(4, "0 1 1 2")
    2
    >>> print_ans(4, "1 1 1 1")
    0
    >>> print_ans(7, "0 3 2 1 2 2 1")
    24
    """
    ar = list(map(int,input_line.split()))
    ngflg = False
    if ar[0] != 0:
        ngflg = True
    k = max(ar)
    tmp_ar = [0] * (k + 1)
    for i in range(1,N):
        tmp_ar[ar[i]] += 1
    if tmp_ar[0] > 0:
        ngflg = True
    if ngflg:
        print("0")
    else:
        ans = 1
        for j in range(2, k + 1):
            ans *=  tmp_ar[j - 1] ** tmp_ar[j]
        print(ans % 998244353)

if __name__ == '__main__':
    N = int(input().rstrip())
    ar = input().rstrip()
    print_ans(N, ar)

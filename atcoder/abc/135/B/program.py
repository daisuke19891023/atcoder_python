import sys
input = sys.stdin.readline
def print_ans(N, p):
    """Test Case
    >>> print_ans(7, "1 2 3 4 5 6 7")
    YES
    >>> print_ans(5, "2 4 3 5 1")
    NO
    >>> print_ans(5, "5 2 3 4 1")
    YES
    """
    pr = list(map(int, p.split()))
    flg = 0
    for i in range(N):
        if i + 1 != pr[i]:
            if flg == 0:
                flg = 1
            elif flg == 1:
                flg = 2
            else:
                flg = 3
    if flg > 2:
        print("NO")
    else:
        print("YES")



if __name__ == '__main__':
    N= int(input().rstrip())
    p = input().rstrip()
    print_ans(N, p)

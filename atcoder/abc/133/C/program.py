import sys
input = sys.stdin.readline
def print_ans(L, R):
    """Test Case
    >>> print_ans(2020, 2040)
    2
    >>> print_ans(4, 5)
    20
    """
    tmp = R - L
    if tmp > 2019:
        print("0")
    else:
        L = L % 2019
        R = L + tmp
        ans = 2019
        flg = False
        for i in range(L, R):
            for k in range(i + 1, R + 1):
                ans = min(ans, (i * k) % 2019)
                if ans == 0:
                    flg = True
                    break
            if flg :
                break
        print(ans)



if __name__ == '__main__':
    L, R = map(int, input().rstrip().split())
    print_ans(L, R)

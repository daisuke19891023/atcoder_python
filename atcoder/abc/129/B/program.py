import sys
input = sys.stdin.readline
def print_ans(n, ws):
    """Test Case
    >>> print_ans(3, [1, 2, 3])
    0
    >>> print_ans(4,[1, 3, 1, 1])
    2
    >>> print_ans(8, [27, 23, 76, 2, 3, 5, 62, 52])
    2
    """
    target = sum(ws) 
    tmp = 0
    ans = 10000
    for w in ws:
        tmp += w
        ans = min(abs(target - (tmp * 2)), ans)
    print(ans)



if __name__ == '__main__':
    n = int(input().rstrip())
    ws = list(map(int, input().rstrip().split()))
    print_ans(n, ws)



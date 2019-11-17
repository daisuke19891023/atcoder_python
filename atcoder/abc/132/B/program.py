import sys
input = sys.stdin.readline
def print_ans(n,pr):
    """Test Case
    >>> print_ans(5, [1, 3, 5, 4, 2])
    2
    >>> print_ans(9, [9, 6, 3, 2, 5, 8, 7, 4, 1])
    5
    """
    ans = 0
    for i in range(1, n-1):
        tmp_arr = sorted([pr[i-1],pr[i],pr[i+1]])
        if  tmp_arr[1] == pr[i]:
            ans +=1
    print(ans)

if __name__ == '__main__':
    n = int(input().rstrip())
    pr = list(map(int, input().rstrip().split()))
    print_ans(n,pr)



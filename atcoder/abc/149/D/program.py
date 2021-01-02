import sys
input = sys.stdin.readline
def check(a, ar):
    if a in ar:
        return True
    else:
        return False

def print_ans(N, ar):
    """Test Case
    >>> print_ans(3, [2, 1, 2])
    1
    >>> print_ans(3, [2, 2, 2])
    -1
    >>> print_ans(10, [3, 1, 4, 1, 5, 9, 2, 6, 5, 3])
    7
    >>> print_ans(1, [1]) 
    0
    """
    if not(check(1, ar)):
        print(-1)
    else:
        index = 0
        ans = 0
        counter = 1
        flg = True
        while flg:
            if check(counter, ar):
                index = ar.index(counter)
                ans += index
                ar = ar[index+1:]
                counter += 1
            else:
                break
        print(ans)




if __name__ == '__main__':
    N = int(input().rstrip())
    ar = list(map(int, input().rstrip().split()))
    print_ans(N, ar)

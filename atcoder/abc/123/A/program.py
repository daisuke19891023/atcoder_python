import sys
input = sys.stdin.readline
def print_ans(ar, k):
    """Test Case
    >>> print_ans([1, 2, 4, 8, 9], 15)
    Yay!
    >>> print_ans([15,18,26,35,36],18)
    :(
    """
    flg = False
    for i in range(4):
        for j in range(i+1,5):
            if ar[j] -ar[i] > k:
                flg = True
                break
        if flg:
            break
    if flg:
        print(":(")
    else:
        print("Yay!")


if __name__ == '__main__':
    ar = [ int(input().rstrip()) for _ in range(5)]
    k = int(input().rstrip())
    print_ans(ar, k)



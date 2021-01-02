import sys
input = sys.stdin.readline
def print_ans(ar):
    """Test Case
    >>> print_ans([5, 7, 9])
    win
    >>> print_ans([13, 7, 2])
    bust
    """
    if sum(ar) >= 22:
        print("bust")
    else:
        print("win")

if __name__ == '__main__':
    ar = list(map(int, input().rstrip().split()))
    print_ans(ar)
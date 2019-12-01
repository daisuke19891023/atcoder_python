import sys
input = sys.stdin.readline
def print_ans(X):
    """Test Case
    >>> print_ans(615)
    1
    >>> print_ans(217)
    0
    """
    A, B = divmod(X, 100)
    taples = (1, 2, 3, 4, 5)
    ans = 0
    for i in taples[::-1]:
        C, B = divmod(B, i)
        ans += C
    if ans <= A:
        print("1")
    else:
        print("0")




if __name__ == '__main__':
    X = int(input().rstrip())
    print_ans(X)

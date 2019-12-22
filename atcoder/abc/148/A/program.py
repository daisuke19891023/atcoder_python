import sys
input = sys.stdin.readline
def print_ans(A,B):
    """Test Case
    >>> print_ans(3, 1)
    2
    >>> print_ans(1, 2)
    3
    """
    ans = [1, 2, 3]
    lists = [A, B]
    for a in ans:
        flg = True
        for b in lists:
            if a == b:
                flg = False
                break
        if flg:
            print(a)

if __name__ == '__main__':
    A = int(input().rstrip())
    B = int(input().rstrip())
    print_ans(A,B)



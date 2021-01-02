import sys
input = sys.stdin.readline
def calc(x):
    if x == 0:
        return 0
    r = x % 4
    if r == 0:
        return x
    elif r == 1:
        return 1
    elif r == 2:
        return 1 ^ x
    else:
        return 0
def print_ans(A, B):
    """Test Case
    >>> print_ans(2, 4)
    5
    >>> print_ans(123, 456)
    435
    >>> print_ans(123456789012, 123456789012)
    123456789012
    """
    tmp = calc(A -1)
    tmp2 = calc(B)
    print(tmp ^ tmp2)

    

if __name__ == '__main__':
    A, B = map(int, input().rstrip().split())
    print_ans(A, B)

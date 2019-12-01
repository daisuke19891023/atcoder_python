import sys
input = sys.stdin.readline
def print_ans(M1, M2):
    """Test Case
    >>> print_ans(11, 11)
    0
    >>> print_ans(11, 12)
    1
    """
    if M1 == M2:
        print("0")
    else:
        print("1")

if __name__ == '__main__':
    M1, D1 = map(int, input().rstrip().split())
    M2, D2 = map(int, input().rstrip().split())
    print_ans(M1, M2)

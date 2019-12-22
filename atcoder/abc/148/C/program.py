import sys
input = sys.stdin.readline
def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a
def print_ans(A, B):
    """Test Case
    >>> print_ans(2, 3)
    6
    >>> print_ans(123, 456)
    18696
    >>> print_ans(100000, 99999)
    9999900000
    """
    print(A * B // gcd(A, B))
if __name__ == '__main__':
    # test
    A, B = map(int, input().rstrip().split())
    print_ans(A, B)
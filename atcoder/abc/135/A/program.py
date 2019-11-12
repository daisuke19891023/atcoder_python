import sys
input = sys.stdin.readline
def print_ans(A, B):
    """Test Case
    >>> print_ans(2, 16)
    9
    >>> print_ans(0, 3)
    IMPOSSIBLE
    >>> print_ans(998244353, 99824435)
    549034394
    """
    if (A + B) % 2 == 0:
        print((A + B) // 2)
    else:
        print("IMPOSSIBLE")

if __name__ == '__main__':
    A, B= map(int,input().rstrip().split())
    print_ans(A, B)

import sys
input = sys.stdin.readline

def print_ans(A, B, K):
    """Test Case
    >>> print_ans(2, 3, 3)
    0 2
    >>> print_ans(500000000000, 500000000000, 1000000000000)
    0 0
    """
    if K <= A:
        print(str(A-K) + " " + str(B))
    elif K <= A + B:
        print("0 " + str(A + B - K))
    elif K > A + B :
        print("0 0")


if __name__ == '__main__':
    A, B, K = map(int, input().rstrip().split())
    print_ans(A, B, K)



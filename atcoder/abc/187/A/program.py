import sys
input = sys.stdin.readline


def print_ans(A, B):
    """Test Case
    >>> print_ans("124", "234")
    9
    """
    ans = max(int(A[0]) + int(A[1]) + int(A[2]), int(B[0]) + int(B[1]) + int(B[2]))
    print(ans)


if __name__ == '__main__':
    A, B = map(str, input().rstrip().split())
    print_ans(A, B)

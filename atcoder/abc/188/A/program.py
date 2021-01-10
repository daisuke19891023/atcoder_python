import sys
input = sys.stdin.readline


def print_ans(A, B):
    """Test Case
    >>> print_ans(3, 5)
    Yes
    >>> print_ans(16, 2)
    No
    """
    if abs(A-B) < 3:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    A, B = map(int, input().rstrip().split())
    print_ans(A, B)

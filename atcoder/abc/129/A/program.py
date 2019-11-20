import sys
input = sys.stdin.readline
def print_ans(ar):
    """Test Case
    >>> print_ans([1, 3, 4])
    4
    >>> print_ans([3, 2, 3])
    5
    """
    print(sum(ar) - max(ar))

if __name__ == '__main__':
    ar = list(map(int, input().rstrip().split()))
    print_ans(ar)



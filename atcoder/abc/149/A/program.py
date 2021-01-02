import sys
input = sys.stdin.readline
def print_ans(S):
    """Test Case
    >>> print_ans(["oder",  "atc"])
    atcoder
    """
    print("".join(S[::-1]))

if __name__ == '__main__':
    S = list(input().rstrip().split())
    print_ans(S)



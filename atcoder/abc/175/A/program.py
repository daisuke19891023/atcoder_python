import sys
input = sys.stdin.readline


def print_ans(S):
    """Test Case
    >>> print_ans("RRS")
    2
    >>> print_ans("SSS")
    0
    >>> print_ans("RSR")
    1
    """
    count = 0
    maximum = 0
    for a in S:
        if a == "R":
            count += 1
        else:
            count = 0
        maximum = max(count, maximum)
    print(maximum)


if __name__ == '__main__':
    S = input().rstrip()
    print_ans(S)

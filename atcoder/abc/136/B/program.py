import sys
input = sys.stdin.readline
def print_ans(N):
    """Test Case
    >>> print_ans(11)
    9
    >>> print_ans(136)
    46
    >>> print_ans(100000)
    90909
    """
    counter = 0
    for i in range(1, N + 1):
        if len(str(i)) % 2 != 0:
            counter +=1
    print(counter)


if __name__ == '__main__':
    N = int(input().rstrip())
    print_ans(N)

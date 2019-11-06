import sys
input = sys.stdin.readline
def print_ans(input_line):
    """Test Case
    >>> print_ans("10")
    5
    >>> print_ans("50")
    13
    >>> print_ans("10000000019")
    10000000018
    """
    N = int(input_line)
    min_ans = N - 1
    for i in range(1,int(N ** 0.5) + 1):
        q, mod= divmod(N,i)
        if mod == 0:
            min_ans = min(min_ans, q + i -2 )
    print(min_ans)

if __name__ == '__main__':
    print_ans(input())

import sys
input = sys.stdin.readline

def print_ans(N, K, M, ar):
    """Test Case
    >>> print_ans(5, 10, 7, [8, 10, 3, 6])
    8
    >>> print_ans(4, 100, 60, [100, 100, 100])
    0
    >>> print_ans(4, 100, 60, [0, 0, 0])
    -1
    """
    must = N * M - sum(ar)
    if must <= 0:
        print('0')
    elif must <= K:
        print(must)
    else:
        print('-1')

if __name__ == '__main__':
    N, K, M = map(int, input().rstrip().split())
    ar = list(map(int, input().rstrip().split()))
    print_ans(N, K, M, ar)



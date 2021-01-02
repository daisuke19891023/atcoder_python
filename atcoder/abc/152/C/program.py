import sys
input = sys.stdin.readline
def print_ans(N, P):
    """Test Case
    >>> print_ans(5, [4, 2, 5, 1, 3])
    3
    >>> print_ans(4, [4, 3, 2, 1])
    4
    >>> print_ans(6, [1, 2, 3, 4, 5, 6])
    1
    >>> print_ans(8, [5, 7, 4, 2, 6, 8, 1, 3])
    4
    >>> print_ans(1, [1])
    1
    """
    min_num = P[0]
    counter = 1
    for i in range(1, N):
        if min_num >= P[i]:
            counter += 1
        min_num = min(min_num, P[i])
    print(counter)



if __name__ == '__main__':
    N = int(input().rstrip())
    P = list(map(int, input().rstrip().split()))
    print_ans(N, P)
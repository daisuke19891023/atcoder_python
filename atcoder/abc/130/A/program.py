import sys
input = sys.stdin.readline
def print_ans(N, X, lr):
    """Test Case
    >>> print_ans(3, 6, [3, 4, 5])
    2
    >>> print_ans(4, 9, [3, 3, 3, 3])
    4
    """
    counter = 1
    ans_sum = 0
    for l in lr:
        ans_sum += l
        if ans_sum > X:
            break
        else:
            counter += 1
    print(counter)

if __name__ == '__main__':
    N, X = map(int, input().rstrip().split())
    lr = list(map(int, input().rstrip().split()))
    print_ans(N, X, lr)



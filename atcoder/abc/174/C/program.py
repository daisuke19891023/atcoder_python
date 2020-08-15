import sys
input = sys.stdin.readline


def print_ans(K):
    """Test Case
    >>> print_ans(101)
    4
    >>> print_ans(2)
    -1
    >>> print_ans(999983)
    999982
    """
    count = 1
    target = 7
    while True:
        if K % 2 == 0:
            print("-1")
            break
        elif target % K == 0:
            print(count)
            break
        else:
            count += 1
            target = target * 10 + 7


if __name__ == '__main__':
    K = int(input().rstrip())
    print_ans(K)

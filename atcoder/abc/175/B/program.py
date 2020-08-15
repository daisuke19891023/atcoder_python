import collections
import itertools
import sys
input = sys.stdin.readline


def check_tri(a, b, c):
    if a + b > c and b + c > a and c + a > b:
        return True
    else:
        return False


def print_ans(lr):
    """Test Case
    >>> print_ans([4, 4, 9, 7, 5])
    5
    >>> print_ans([4, 5, 4, 3, 3, 5])
    8
    >>> print_ans([9, 4, 6, 1, 9, 6, 10, 6, 6, 8])
    39
    >>> print_ans([1,1])
    0
    """
    ans = 0
    c = collections.Counter(lr)
    target = itertools.combinations(list(c.keys()), 3)
    for t in target:
        if check_tri(t[0], t[1], t[2]):
            tmp = (c[t[0]] * c[t[1]] * c[t[2]])
            ans += tmp
    print(ans)


if __name__ == '__main__':
    N = int(input().rstrip())
    lr = list(map(int, input().rstrip().split()))
    print_ans(lr)

import sys
input = sys.stdin.readline
def print_ans(K, X):
    """Test Case
    >>> print_ans(3, 7)
    5 6 7 8 9
    >>> print_ans(4, 0)
    -3 -2 -1 0 1 2 3
    >>> print_ans(1, 100)
    100
    """
    ans = [i for i in range(X - K + 1, X + K)]
    print(" ".join(list(map(str,ans))))
if __name__ == '__main__':
    K, X = map(int,input().rstrip().split())
    print_ans(K, X)

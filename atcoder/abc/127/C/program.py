import sys
input = sys.stdin.readline
def print_ans(W, H, x, y):
    """Test Case
    >>> print_ans(2, 3, 1, 2)
    3.000000 0
    >>> print_ans(2, 2, 1, 1)
    2.000000 1
    """
    area = W * H / 2
    whether = "1" if x * 2 == W and y *2 == H else "0"
    print("{} {}".format(str(area), whether)) 

if __name__ == '__main__':
    W, H, x, y = map(int, input().rstrip().split())
    print_ans(W, H, x, y)



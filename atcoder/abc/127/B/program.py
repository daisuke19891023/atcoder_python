import sys
input = sys.stdin.readline
import numpy as np
def print_ans(r, D, x):
    """Test Case
    >>> print_ans(2, 10, 20)
    30
    50
    90
    170
    330
    650
    1290
    2570
    5130
    10250
    >>> print_ans(4, 40, 60)
    200
    760
    3000
    11960
    47800
    191160
    764600
    3058360
    12233400
    48933560
    """
    for _ in range(10):
        x = r * x - D
        print(x)

if __name__ == '__main__':
    r, D, x = map(int, input().rstrip().split())
    print_ans(r, D, x)



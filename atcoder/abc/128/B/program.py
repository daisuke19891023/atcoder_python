import sys
input = sys.stdin.readline
import numpy as np
def print_ans(N, ar):
    """Test Case
    >>> print_ans(6,[["khabarovsk",-20, 1], ["moscow",-10, 2], ["kazan",-50, 3], ["kazan",-35, 4], ["moscow",-60, 5], ["khabarovsk",-40, 6]])
    3
    4
    6
    1
    5
    2
    >>> print_ans(10, [["yakutsk", -10, 1 ], ["yakutsk", -20, 2 ], ["yakutsk", -30, 3 ], ["yakutsk", -40, 4 ], ["yakutsk", -50, 5 ], ["yakutsk", -60, 6 ], ["yakutsk", -70, 7 ], ["yakutsk", -80, 8 ], ["yakutsk", -90, 9 ], ["yakutsk", -100,10]])
    10
    9
    8
    7
    6
    5
    4
    3
    2
    1
    """
    ans = sorted(ar)
    for a in ans:
        print(a[2])

if __name__ == '__main__':
    N = int(input().rstrip())
    ar = []
    for i in range(N):
        s, p = input().rstrip().split()
        p = int(p)
        ar.append([s, -p, i + 1])
    print_ans(N, ar)



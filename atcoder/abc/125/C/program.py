import sys
input = sys.stdin.readline
import math
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN
from fractions import *
def print_ans(N, a_list):
    """Test Case
    >>> print_ans(3, [0, 7, 6, 8, 0])
    2
    >>> print_ans(3, [0, 12, 15, 18, 0])
    6
    >>> print_ans(2, [0, 1000000000, 1000000000,0])
    1000000000
    """
    l_list = [0 for _ in range(N + 2)]
    r_list = [0 for _ in range(N + 2)]
    for i in range(1, N + 1):
        l_list[i] = gcd(l_list[i-1], a_list[i])
    for i in range(N, 0, -1):
            r_list[i] = gcd(r_list[i + 1], a_list[i])
    m_list = [0 for _ in range(N + 1)]
    for i in range(1, N + 1):
        m_list[i] = gcd(l_list[i - 1],r_list[i+ 1])
    print(max(m_list))

if __name__ == '__main__':
    N = int(input().rstrip())
    a_list = [0] + list(map(int, input().rstrip().split())) + [0]
    print_ans(N, a_list)

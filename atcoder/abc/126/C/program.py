import sys
input = sys.stdin.readline
import math
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN

def print_ans(N, K):
    """Test Case
    >>> print_ans(3, 10)
    0.145833333333
    >>> print_ans(100000, 5)
    0.999973749998
    """
    prob = Decimal(1 / N)
    b = Decimal(math.log2(K))
    ans = 0
    for i in range(1, N + 1):
        if i >= K:
            ans += 1
        else:
            k = Decimal(math.ceil(b - Decimal((math.log2(i)))))
            ans += Decimal(2 ** (-k) ) 
    print(Decimal(ans * prob).quantize(Decimal('0.000000000001'), rounding=ROUND_HALF_EVEN))



if __name__ == '__main__':
    N, K = map(int, input().rstrip().split())
    print_ans(N, K)

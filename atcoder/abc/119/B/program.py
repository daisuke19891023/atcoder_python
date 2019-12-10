import sys
input = sys.stdin.readline
from decimal import Decimal,ROUND_HALF_UP
def print_ans(N, ar):
    """Test Case
    >>> print_ans(2, [["10000", "JPY"],["0.10000000", "BTC"]])
    48000.0
    >>> print_ans(3, [["100000000", "JPY"],["100.00000000", "BTC"],["0.00000001", "BTC"]])
    138000000.0038
    """
    ans = 0.0
    for a in ar:
        if a[1] == 'BTC':
            ans += float(Decimal(str(float(a[0]) * 380000.0)).quantize(Decimal('0.00001'), rounding=ROUND_HALF_UP) )
        else:
            ans += float(a[0])
    print(ans)


if __name__ == '__main__':
    N = int(input().rstrip())
    ar = [input().rstrip().split() for _ in range(N)]
    print_ans(N, ar)

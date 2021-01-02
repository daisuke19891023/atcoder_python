import sys
input = sys.stdin.readline
import numpy as np
from math import factorial
def cmb(n, r, mod):
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod
mod = 10**9+7 #出力の制限
N = 10**6
g1 = [1, 1] # 元テーブル
g2 = [1, 1] #逆元テーブル
inverse = [0, 1] #逆元テーブル計算用テーブル

for i in range( 2, N + 1 ):
    g1.append( ( g1[-1] * i ) % mod )
    inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
    g2.append( (g2[-1] * inverse[-1]) % mod )
def print_ans(X, Y):
    """Test Case
    >>> print_ans(3, 3)
    2
    >>> print_ans(2, 2)
    0
    >>> print_ans(999999, 999999)
    151840682
    """
    A = np.array([[1, 2],[2, 1]])
    B = np.array([X, Y])
    X = np.linalg.solve(A, B)
    if X[0].is_integer() and X[1].is_integer() :
        print(cmb(int(X[0] + X[1]),int(X[0]),mod))
    else:
        print("0")


if __name__ == '__main__':
    X, Y = map(int, input().rstrip().split())
    print_ans(X, Y)

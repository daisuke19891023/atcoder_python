import sys
input = sys.stdin.readline
import itertools
def cmb(n, r, mod):
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod

mod = 10**9+7 #出力の制限
N = 2 * 10**5
g1 = [1, 1] # 元テーブル
g2 = [1, 1] #逆元テーブル
inverse = [0, 1] #逆元テーブル計算用テーブル

for i in range( 2, N + 1 ):
    g1.append( ( g1[-1] * i ) % mod )
    inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
    g2.append( (g2[-1] * inverse[-1]) % mod )
def print_ans(NN, K):
    """Test Case
    >>> print_ans(3, 2)
    10
    """
    ans = 0
    for i in range(K,NN+2):
        a = cmb(NN+1,i,mod)
        print(a)

if __name__ == '__main__':
    NN, K = map(int, input().rstrip().split())
    print_ans(NN, K)
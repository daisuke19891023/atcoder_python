import sys
input = sys.stdin.readline


def check_tri(a, b, c):
    if a + b > c and b + c > a and c + a > b:
        return True
    else:
        return False


def print_ans(N, L):
    """Test Case
    >>> print_ans(3, [[0 ,0],[1 ,2],[2 ,1]])
    2
    >>> print_ans(1, [[-691, 273]])
    0
    >>> print_ans(10,[[-31 ,-35],[8 ,-36],[22 ,64],[5 ,73],[-14 ,8],[18 ,-58],[-41 ,-85],[1 ,-88],[-21 ,-85],[-11 ,82]])
    11
    """
    ans = 0
    for i in range(N-1):
        for j in range(i+1, N):
            flg = (L[i][1] - L[j][1]) / (L[i][0] - L[j][0])
            if abs(flg) <= 1:
                ans += 1
    print(ans)


if __name__ == '__main__':
    N = int(input().rstrip())
    L = [list(map(int, input().split())) for i in range(N)]
    print_ans(N, L)

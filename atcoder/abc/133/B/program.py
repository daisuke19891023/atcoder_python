import sys
input = sys.stdin.readline
import numpy as np
def print_ans(N, D, dr):
    """Test Case
    >>> print_ans(3, 2, [[1, 2], [5, 5], [-2, 8]])
    1
    >>> print_ans(3, 4, [[-3, 7, 8, 2], [-12, 1, 10, 2], [-2, 8, 9, 3]])
    2
    >>> print_ans(5, 1, [[1],[2],[3],[4],[5]])
    10
    """
    dr = [np.array(d) for d in dr]
    ans = 0
    for i in range(N-1):
        for k in range(i + 1, N):
            multi_ar = dr[i] - dr[k] 
            abs_tmp = float(np.sum(multi_ar ** 2) ** (1/2))
            if(abs_tmp.is_integer()):
                ans += 1
    print(ans)



if __name__ == '__main__':
    N, D = map(int, input().rstrip().split())
    dr = [list(map(int, input().rstrip().split())) for _ in range(N)]
    print_ans(N, D, dr)

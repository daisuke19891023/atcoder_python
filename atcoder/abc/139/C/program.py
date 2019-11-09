import sys
input = sys.stdin.readline
import math
def print_ans(N,H):
    """Test Case
    >>> print_ans(5, "10 4 8 7 3")
    2
    >>> print_ans(7, "4 4 5 6 6 5 5")
    3
    >>> print_ans(4, "1 2 3 4")
    0
    """
    h_arr = list(map(int,H.split()))
    ans = 0
    ofs = 0
    for i in range(N):
        if ofs == i:
            tmp = h_arr[i]
            tmp_ans = 0
            for k in range(i + 1, N):
                ofs += 1
                if tmp >= h_arr[k]:
                    tmp_ans += 1
                    tmp = h_arr[k]
                else:
                    break
            ans = max(ans,tmp_ans)
    print(ans)
            


if __name__ == '__main__':
    N = int(input().rstrip())
    H = input().rstrip()
    print_ans(N,H)
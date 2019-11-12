import sys
input = sys.stdin.readline
def print_ans(N, A, B):
    """Test Case
    >>> print_ans(2, "3 5 2", "4 5")
    9
    >>> print_ans(3, "5 6 3 8", "5 100 8")
    22
    >>> print_ans(2, "100 1 1", "1 100")
    3
    """
    ar = list(map(int, A.split()))
    br = list(map(int, B.split()))
    ans = 0
    for i in range(N):
        if br[i] < ar[i]:
            ans += br[i]
        else:
            ans += ar[i]
            br[i] -= ar[i]
            if ar[i + 1] <= br[i]:
                ans += ar[i + 1]
                ar[i + 1] = 0
            else:
                ans += br[i]
                ar[i + 1] -= br[i]  
    print(ans)

if __name__ == '__main__':
    N= int(input().rstrip())
    A = input().rstrip()
    B = input().rstrip()    
    print_ans(N, A, B)

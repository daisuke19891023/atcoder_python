import sys
input = sys.stdin.readline
def print_ans(N, H):
    """Test Case
    >>> print_ans(5, [1, 2, 1, 1, 3])
    Yes
    >>> print_ans(4, [1, 3, 2, 1])
    No
    >>> print_ans(5, [1, 2, 3, 4, 5])
    Yes
    >>> print_ans(1, [1000000000])
    Yes
    """
    if N == 1 :
        print("Yes")
    else:
        tmp_max = 0
        for i in range(N - 1):
            if (H[i] > H[i + 1] and H[i] - 1 > H[i + 1] ) or tmp_max > H[i + 1]  :
                print("No")
                break
            else:
                if H[i] < H[i + 1]:
                    H[i + 1] -= 1
                    tmp_max = H[i + 1]
            if i == N -2:
                print("Yes")



if __name__ == '__main__':
    N = int(input().rstrip())
    H = list(map(int,input().rstrip().split()))
    print_ans(N, H)

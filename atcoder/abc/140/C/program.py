import sys
input = sys.stdin.readline
def print_ans(N,B):
    """Test Case
    >>> print_ans(3,"2 5")
    9
    >>> print_ans(2,"3")
    6
    >>> print_ans(6,"0 153 10 10 23")
    53
    """
    B_arr = list(map(int,B.split()))
    A_arr = [0] * N
    for i in range(N - 1):
        A_arr[i + 1] = B_arr[i]
        if i == 0:
            A_arr[i] = B_arr[i]
        else:
            A_arr[i] = min(A_arr[i],B_arr[i])
    print(sum(A_arr))
if __name__ == '__main__':
    N = int(input().rstrip())
    B = input().rstrip()
    print_ans(N,B)
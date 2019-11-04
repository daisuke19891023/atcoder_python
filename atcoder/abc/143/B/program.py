import sys
input = sys.stdin.readline
def print_ans(N,input_line):
    """Test Case
    >>> print_ans(3,"3 1 2")
    11
    >>> print_ans(7,"5 0 7 8 3 3 2")
    312
    """
    arr = list(map(int,input_line.split()))
    res = 0
    for i in range(N):
        for j in range(i+1,N):
            res += arr[i] * arr[j]
    print(str(res))
if __name__ == '__main__':
    N = int(input())
    input_line = input()
    print_ans(N,input_line)
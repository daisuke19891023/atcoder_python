import sys
input = sys.stdin.readline
def print_ans(input_line,input_arr):
    """Test Case
    >>> print_ans("4 150","150 140 100 200")
    2
    >>> print_ans("1 500","499")
    0
    >>> print_ans("5 1","100 200 300 400 500")
    5
    """
    N, K = list(map(int,input_line.split()))
    arr = list(map(int,input_arr.split()))
    ans = filter(lambda x:x >= K, arr)
    print(len(list(ans)))

if __name__ == '__main__':
    N = input()
    arr = input()
    print_ans(N,arr)
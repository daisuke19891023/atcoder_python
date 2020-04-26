import sys
input = sys.stdin.readline
def print_ans(N, ar):
    """Test Case
    >>> print_ans(3, ["apple", "orange", "apple"])
    2
    >>> print_ans(5,["grape" ,"grape" ,"grape" ,"grape" ,"grape"])
    1
    """
    print(len(set(ar)))
    

if __name__ == '__main__':
    N = int(input().rstrip())
    ar = [input().rstrip() for _ in range(N) ]
    print_ans(N, ar)



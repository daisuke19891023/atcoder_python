import sys
input = sys.stdin.readline
def print_ans(A, B, C, D):
    """Test Case
    >>> print_ans(10, 9, 10, 10)
    No
    >>> print_ans(46, 4, 40, 5)
    Yes
    """
    while True:
        #Yes perttern
        C = C - B
        if(C <= 0):
            print("Yes")
            break
        #No perttern
        A = A - D
        if(A <= 0):
            print("No")
            break



if __name__ == '__main__':
    A, B, C, D = map(int, input().rstrip().split())
    print_ans(A,B, C, D)



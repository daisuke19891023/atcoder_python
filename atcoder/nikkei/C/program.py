import sys
input = sys.stdin.readline
import numpy as np
def print_ans(N, A, B):
    """Test Case
    >>> print_ans(3, "1 3 2", "1 2 3")
    Yes
    >>> print_ans(3, "1 2 3", "2 2 2")
    No
    >>> print_ans(6, "3 1 2 6 3 4", "2 2 8 3 4 3")
    Yes
    """
    ar = np.array(A.split(),'int32')
    br = np.array(B.split(),'int32')
    I = br.argsort()
    br = br[I]
    ar = ar[I]
    Asorted = np.sort(ar)
    if ( Asorted> br).any():
        print("No")
    else:
        
        #N-1回の置換で成立する
        if (Asorted[1:] < br[:-1]).any():
            print("Yes") 
 

if __name__ == '__main__':
    N = int(input().rstrip())
    A = input().rstrip()
    B = input().rstrip()
    print_ans(N, A, B)
import sys
input = sys.stdin.readline
import itertools
def print_ans(N, ar):
    """Test Case
    >>> print_ans(5, [1, 1, 2, 2])
    2
    2
    0
    0
    0
    >>> print_ans(10, [1,1,1,1,1,1,1,1,1])
    9
    0
    0
    0
    0
    0
    0
    0
    0
    0
    >>> print_ans(7, [1,2,3,4,5,6])
    1
    1
    1
    1
    1
    1
    0
    """
    ans_list = [0] * N
    gr = itertools.groupby(sorted(ar))
    for key, group in gr:
        ans_list[key-1] = (len(list(group)))
    for ans in ans_list:
        print(ans)
    
    



    
    

if __name__ == '__main__':
    N = int(input().rstrip())
    ar = list(map(int, input().rstrip().split()))
    print_ans(N, ar)



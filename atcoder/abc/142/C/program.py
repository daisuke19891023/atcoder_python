import sys
input = sys.stdin.readline
import numpy as np
def print_ans(input_line):
    """Test Case
    >>> print_ans("2 3 1")
    3 1 2
    >>> print_ans("1 2 3 4 5")
    1 2 3 4 5
    >>> print_ans("8 2 7 3 4 5 6 1")
    8 2 4 5 6 7 3 1
    """
    arr = np.array(list(map(int,input_line.split())))
    arr_sort = np.argsort(arr) + 1
    arr_str = list(map(str,arr_sort.tolist()))
    print(" ".join(arr_str))

if __name__ == '__main__':
    N = int(input())
    input_line = input()
    print_ans(input_line)
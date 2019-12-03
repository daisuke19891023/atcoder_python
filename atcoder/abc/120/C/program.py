import sys
input = sys.stdin.readline
import re
def print_ans(S):
    """Test Case
    >>> print_ans("0011")
    4
    >>> print_ans("11011010001011")
    12
    >>> print_ans("0")
    0
    """
    list_0 = []
    list_1 = []
    for s in S:
        if s =="0":
            list_0.append(s)
        else:
            list_1.append(s)
    print(min(len(list_0), len(list_1)) * 2)
        


if __name__ == '__main__':
    S = input().rstrip()
    print_ans(S)

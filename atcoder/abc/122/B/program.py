import sys
input = sys.stdin.readline
tuples = ("A", "C", "G", "T")
def print_ans(B):
    """Test Case
    >>> print_ans("ATCODER")
    3
    >>> print_ans("HATAGAYA")
    5
    >>> print_ans("SHINJUKU")
    0
    """
    max_len = 0
    tmp = 0
    for b in B:
        if b in tuples:
            tmp += 1
            max_len = max(max_len, tmp)
        else:
            tmp = 0
    print(max_len)

    

if __name__ == '__main__':
    B = input().rstrip()
    print_ans(B)

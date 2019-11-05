from itertools import groupby
def print_ans(input_line):
    """Test Case
    >>> print_ans("aabbbbaaca")
    5
    >>> print_ans("aaaaa")
    1
    >>> print_ans("xxzaffeeeeddfkkkkllq")
    10
    """
    print(len(list(groupby(input_line))))

if __name__ == '__main__':
    N = int(input())
    s = input()
    print_ans(s)
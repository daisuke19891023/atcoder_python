def print_ans(input_line):
    """Test Case
    >>> print_ans("12 4")
    4
    """
    A, B = list(map(int,input_line.split()))
    print(str(max(0,A - B * 2)))

if __name__ == '__main__':
    input_line = input()
    print_ans(input_line)
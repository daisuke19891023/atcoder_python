import sys
input = sys.stdin.readline
def print_ans(input_line):
    """Test Case
    >>> print_ans("Sunny")
    Cloudy
    >>> print_ans("Rainy")
    Sunny
    """
    if input_line == "Sunny":
        print("Cloudy")
    elif input_line == "Rainy":
        print("Sunny")
    else:
        print("Rainy")


if __name__ == '__main__':
    input_line = input().rstrip()
    print_ans(input_line)

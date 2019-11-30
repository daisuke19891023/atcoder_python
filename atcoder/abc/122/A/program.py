import sys
input = sys.stdin.readline
dictionary = {"A":"T","T":"A","C":"G","G":"C"}
def print_ans(b):
    """Test Case
    >>> print_ans("A")
    T
    >>> print_ans("G")
    C
    """
    print(dictionary[b])


if __name__ == '__main__':
    b = input().rstrip()
    print_ans(b)



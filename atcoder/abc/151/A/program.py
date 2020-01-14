import sys
input = sys.stdin.readline
char_list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
def print_ans(S):
    """Test Case
    >>> print_ans("a")
    b
    """
    a = S.upper()
    for i, b in enumerate(char_list):
        if b == a:
            print(char_list[i+1].lower())
        


if __name__ == '__main__':
    S = input().rstrip()
    print_ans(S)



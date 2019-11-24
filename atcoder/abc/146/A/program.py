import sys
input = sys.stdin.readline
holidays = ['','SAT', 'FRI','THU','WED','TUE','MON','SUN']
def print_ans(S):
    """Test Case
    >>> print_ans("SAT")
    1
    >>> print_ans("SUN")
    7
    """
    for i, day in enumerate(holidays):
        if S == day:
            print(i)

if __name__ == '__main__':
    S = input().rstrip()
    print_ans(S)



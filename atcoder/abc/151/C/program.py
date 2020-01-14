import sys
input = sys.stdin.readline
from itertools import groupby
from operator import itemgetter
def print_ans(N, M, ar):
    """Test Case
    >>> print_ans(2, 5, [['1', 'WA'], ['2', 'WA'], ['2', 'AC'], ['2', 'WA'], ['1', 'AC']])
    2 2
    >>> print_ans(100000, 3, [['7777', 'AC'], ['7777', 'AC'], ['7777', 'AC']])
    1 0
    >>> print_ans(6, 0, [])
    0 0
    """
    correct = 0
    wrong = 0
    ar = sorted(ar, key=itemgetter(0))
    if M == 0:
        print(0, 0)
    else:
        for (k, g) in groupby(ar, key=itemgetter(0)):
            tmp_wrong = 0
            ac_flg = False
            for item in g:
                if item[1] == "AC":
                    correct += 1
                    ac_flg = True
                    break
                else:
                    tmp_wrong += 1
            if ac_flg == True:
                wrong += tmp_wrong
        print("{} {}".format(correct, wrong))
if __name__ == '__main__':
    N, M = map(int, input().rstrip().split())
    if M == 0:
        ar = []
    else:
        ar = [list(map(str, input().rstrip().split())) for i in range(M)]
    print_ans(N, M, ar)
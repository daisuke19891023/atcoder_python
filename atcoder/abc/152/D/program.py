import sys
input = sys.stdin.readline
import itertools
from itertools import groupby
# def under10(N):
#     if N < 10:
#     	return False, N
# 	else:
#     	return True, 9
def makelist(N):
    math_list = [[0 for i in range(10)] for j in range(10)]
    # target_list = itertools.combinations(range(1, 10), 2)
    # for v in target_list:
    #     print(v)
    # print(math_list)
    target_list = []
    for i in range(1, N + 1):
        left = int(str(i)[0])
        right = int(str(i)[-1])
        math_list[left][right] += 1
        target_list.append([left, right])
    return target_list

                
def print_ans(N):
    """Test Case
    >>> print_ans(25)
    17
    >>> print_ans(1)
    1
    >>> print_ans(100)
    108
    """
    groups = []
    uniquekeys = []
    ans_list = [[0 for i in range(10)] for j in range(10)]
    target_list = sorted(makelist(N))
    for (k, g) in groupby(target_list):
        uniquekeys.append(k)
        counter = 0
        for item in g:
            counter += 1
        groups.append(counter)
        ans_list[k[0]][k[1]] = counter
    # d = dict(zip(uniquekeys,groups))
    ans = 0
    for i in range(1, 10):
        for j in range(i, 10):
            base = ans_list[i][j]
            rev = ans_list[j][i]
            # if base == 0 and rev != 0:
            #     tmp = rev
            # elif base != 0 and rev == 0:
            #     tmp = base
            # else:
            #     tmp = base * rev
            tmp = base * rev
            ans += tmp
    print(ans)

if __name__ == '__main__':
    N = int(input().rstrip())
    print_ans(N)
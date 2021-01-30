
import itertools
import sys
import copy
input = sys.stdin.readline


def proccess(source: list, a: int, b: int):
    target = copy.deepcopy(source)
    ret_list = []
    for s in source:
        s.append(a)
        # s.sort()
        ret_list.append(list(set(s)))
        # ret_list.append(s)
    for t in target:
        t.append(b)
        # t.sort()
        ret_list.append(list(set(t)))
        # ret_list.append(t)

    # ret_list = list(set(ret_list))
    return ret_list


def sort_by_length(ar: list, N: int):
    ar = list(filter(lambda x: len(x) >= N, ar))
    # ar.sort(key=lambda x: len(x), reverse=True)
    return ar


def print_ans(N, cons, pepole):
    """Test Case
    >>> print_ans(4, [(1,2), (1,3), (2,4), (3,4)], [(1, 2), (1, 3), (2, 3)])
    2
    >>> print_ans(4, [(1,2), (1,3), (2,4), (3,4)], [(3, 4), (1, 2), (2, 4), (2, 4)])
    4
    >>> print_ans(6, [(2, 3), (4, 6), (1, 2), (4, 5), (2, 6), (1, 5), (4, 5), (1, 3), (1, 2), (2, 6), (2, 3), (2, 5)], [(3, 5), (1, 4), (2, 6), (4, 6), (5, 6)])
    9
    """
    # boll_list = []
    # first = pepole.pop(0)
    # # print(pepole)
    # boll_list.append([first[0]])
    # boll_list.append([first[1]])
    # for a, b in pepole:
    #     boll_list = proccess(boll_list, a, b)
    # target_list = list(set(list(map(tuple, boll_list))))
    # target_list = sort_by_length(target_list, len(pepole)+1)
    # # print(target_list)
    # ans = 0
    # # for t in target_list:
    # #     tmp_ans = 0
    # #     all = itertools.combinations(t, 2)
    # #     for x in all:
    # #         if x in cons:
    # #             tmp_ans += 1
    # #     ans = max(ans, tmp_ans)
    # # print(ans)
    # for t in target_list:
    #     tmp_ans = 0
    #     for con in cons:
    #         if (con[0] in t) and (con[1] in t):
    #             tmp_ans += 1
    #     ans = max(ans, tmp_ans)
    # print(ans)
    lists = itertools.product(*pepole)
    ans = 0
    for a in lists:
        balls = set(a)
        cnt = sum(A in balls and B in balls for A, B in cons)
        ans = max(ans, cnt)
    print(ans)


if __name__ == '__main__':
    N, M = map(int, input().rstrip().split())
    cons = [tuple(map(int, input().split())) for i in range(M)]
    K = int(input().rstrip())
    pepole = [tuple(map(int, input().split())) for i in range(K)]
    print_ans(N, cons, pepole)

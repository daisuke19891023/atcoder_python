import copy
import sys
input = sys.stdin.readline


def proccess(source: list, a: int, b: int):
    target = copy.deepcopy(source)
    ret_list = []
    for s in source:
        s.append(a)
        ret_list.append(s)
    for t in target:
        t.append(b)
        ret_list.append(t)
    return ret_list


def print_ans(N, S, D, L):
    """Test Case
    >>> print_ans(4, 9, 9, [[5, 5],[15, 5],[5, 15],[15, 15]])
    Yes
    >>> print_ans(3, 691, 273, [[691, 997], [593, 273], [691, 273]] )
    No
    >>> print_ans(7, 100, 100, [[10, 11], [12, 67], [192, 79], [154, 197], [142, 158], [20, 25], [17, 108]])
    Yes
    """
    flg = True
    for x, y in L:
        if (x < S) and (y > D):
            print("Yes")
            flg = False
            break
    if flg:
        print("No")


if __name__ == '__main__':
    N, S, D = map(int, input().rstrip().split())
    L = [list(map(int, input().split())) for i in range(N)]
    print_ans(N, S, D, L)

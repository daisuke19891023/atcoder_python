import sys
input = sys.stdin.readline


def print_ans(N, lr):
    """Test Case
    >>> print_ans(6,["a","!a","b","!c","d","!d"])
    a
    >>> print_ans(10,["red","red","red","!orange","yellow","!blue","cyan","!green","brown","!gray"])
    satisfiable
    """
    ex_list = []
    non_ex_list = []
    flg = True
    for l in lr:
        if l[0] == "!":
            ex_list.append(l[1:])
        else:
            non_ex_list.append(l)
    set_list = set(ex_list) & set(non_ex_list)
    if len(set_list) == 0:
        print("satisfiable")
    else:
        print(list(set_list)[0])
    # for e in ex_list:
    #     if e in non_ex_list:
    #         print(e)
    #         flg = False
    #         break
    # if flg:
    #     print("satisfiable")


if __name__ == '__main__':
    N = int(input().rstrip())
    L = [input().rstrip() for i in range(N)]
    print_ans(N, L)

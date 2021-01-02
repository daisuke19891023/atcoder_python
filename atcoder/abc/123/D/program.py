import sys
input = sys.stdin.readline

def print_ans(N, K, S):
    """Test Case
    >>> print_ans(14, 2, "11101010110011")
    8
    >>> print_ans(5, 1, "00010")
    4
    >>> print_ans(1, 1, "1")
    1
    """
    list_zero = []
    list_one = []
    first = S[0]
    tmp_zero = ""
    tmp_one = ""
    ans = 0
    if len(S) == 1:
        print("1")
    else:
        if  S[0] == "0":
            tmp_zero = tmp_zero + S[0]
        else:
            tmp_one = tmp_one + S[0]
        #create 0 1 list
        for i in range(1, N):
            if S[i] == "0":
                tmp_zero = tmp_zero + S[i]
                if S[i - 1] != S[i]:
                    list_one.append(len(tmp_one))
                    tmp_one = ""
            else:
                tmp_one = tmp_one + S[i]
                if S[i - 1] != S[i]:
                    list_zero.append(len(tmp_zero))
                    tmp_zero = ""
        if len(tmp_zero) > 0:
            list_zero.append(len(tmp_zero))
        if len(tmp_one) > 0:
            list_one.append(len(tmp_one))

        if first == "1":
            for i in range(len(list_zero) - K + 1):
                ans = max(ans, sum(list_zero[i:i+K]) + sum(list_one[i:i+K+1]) )
        else:
            for i in range(len(list_zero) - K + 1):
                ans = max(ans, sum(list_zero[i:i+K]) + sum(list_one[i:i+K+1]) )
        print(ans)

    

if __name__ == '__main__':
    N, K = map(int, input().rstrip().split())
    S = input().rstrip()
    print_ans(N, K, S)

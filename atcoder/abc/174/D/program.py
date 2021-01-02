import sys
input = sys.stdin.readline
    
def print_ans(S):
    """Test Case
    >>> print_ans('1817181712114')
    3
    >>> print_ans('14282668646')
    2
    >>> print_ans('2119')
    0
    """
    target_list = []
    itr = 2019
    for i in range(1, 9906):
        tmp = i * itr
        if tmp > int(S):
            break
        elif '0' in list([s for s in str(tmp)]):
            continue
        else:
            target_list.append(tmp)
    ans = 0
    if len(S) <= 3:
        print(0)
    else:
        for i in range(len(S)-3):
            if S[i] == 1:
                length = min(9, len(S) -i)
                for k in range(i + 2, length):
                    tmp = S[i:k+1]
                    if int(tmp) in target_list:
                        ans = ans + 1
            else:    
                length = min(8, len(S) -i + 1)
                for j in range(i + 2, length):
                    tmp = S[i:j+1]
                    if int(tmp) in target_list:
                        ans = ans + 1
        print(ans)
            
            

if __name__ == '__main__':
    S = input().rstrip()
    print_ans(S)
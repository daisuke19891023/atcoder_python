import sys
input = sys.stdin.readline
import numpy as np
base_list = np.array(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'])
dict_list = []
dict_list.append(base_list)
for i in range(26):
    tmp_char = dict_list[i][0]
    tmp_list = dict_list[i][1:]
    tmp_list = np.append(tmp_list,tmp_char)
    dict_list.append(tmp_list)

def print_ans(N, sr):
    """Test Case
    >>> print_ans(2, ['A', 'B', 'C', 'X', 'Y', 'Z'])
    CDEZAB
    >>> print_ans(0, ['A', 'B', 'C','X', 'Y', 'Z'])
    ABCXYZ
    """
    idx_list = []
    for s in sr:
        tmp = np.where(base_list == s)[0]
        idx_list.append(int(tmp))
    ans = ''.join(dict_list[N][idx_list])
    print(ans)

if __name__ == '__main__':
    N = int(input().rstrip())
    tmp_s= input().rstrip()
    sr = []
    for s in tmp_s:
        sr.append(s)
    print_ans(N, sr)



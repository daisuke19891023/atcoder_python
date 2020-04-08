import sys
input = sys.stdin.readline
import numpy as np
def print_ans(N, ar):
    """Test Case
    >>> print_ans(7, ["beat", "vet", "beet", "bed", "vet", "bet", "beet"])
    beet
    vet
    >>> print_ans(8, ["buffalo", "buffalo", "buffalo", "buffalo", "buffalo", "buffalo", "buffalo", "buffalo"])
    buffalo
    >>> print_ans(7, ["bass", "bass", "kick", "kick", "bass", "kick", "kick"])
    kick
    >>> print_ans(4, ["ushi", "tapu", "nichia", "kun"])
    kun
    nichia
    tapu
    ushi
    """
    dict = {}
    for a in ar:
        if a in dict:
            dict[a] = dict[a] + 1
        else:
            dict[a] = 0
    max_val = max(dict.values())
    key_list = sorted([key for key in dict if dict[key] == max_val])
    for key in key_list:
        print(key)


    
    

if __name__ == '__main__':
    N = int(input().rstrip())
    ar = [ input().rstrip() for _ in range(N)]
    print_ans(N, ar)



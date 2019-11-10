import sys
input = sys.stdin.readline
from collections import Counter
def print_ans(N, sr):
    """Test Case
    >>> print_ans(3, ["acornistnt", "peanutbomb", "constraint"])
    1
    >>> print_ans(2, ["oneplustwo", "ninemodsix"])
    0
    >>> print_ans(5,["abaaaaaaaa","oneplustwo","aaaaaaaaba","twoplusone","aaaabaaaaa"]) 
    4
    """
    for i in range(N):
        sr[i] = "".join(sorted(sr[i]))
    C = Counter(sr)
    ans = 0
    for v in C.values():
        ans += v * (v - 1) // 2
    print(ans)
if __name__ == '__main__':
    N = int(input().rstrip())
    sr = [ input().rstrip() for _ in range(N)]
    print_ans(N, sr)

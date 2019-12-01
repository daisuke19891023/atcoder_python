import sys
input = sys.stdin.readline
lists = ['{0:03d}'.format(i) for i in range(1000)]
import re
def check(target, a):
    ans = re.search(a, target)
    if ans == None:
        return None
    else:
        return target[ans.start()+1:]

def print_ans(N, S):
    """Test Case
    >>> print_ans(4, "0224")
    3
    >>> print_ans(6, "123123")
    17
    >>> print_ans(19, "3141592653589793238")
    329
    """
    ans = 0
    for a in lists:
        tmp = S
        for i in range(3):
            tmp = check(tmp, a[i])
            if tmp == None:
                break
        if tmp != None:
            ans += 1
    print(ans)
    
if __name__ == '__main__':
    N = int(input().rstrip())
    S = input().rstrip()
    print_ans(N, S)

import sys
input = sys.stdin.readline
import math
import itertools
def distance(N, ar):
    table = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i != j:
                dx = ar[i][0] - ar[j][0]
                dy = ar[i][1] - ar[j][1]
                table[i][j] = math.sqrt(dx * dx + dy * dy)
    return table    

def print_ans(N, ar):
    """Test Case
    >>> print_ans(3, [[0, 0],[1, 0],[0, 1]])
    2.2761423749
    >>> print_ans(2, [[-879, 981], [-866, 890]])
    91.9238815543
    >>> print_ans(8, [[-406, 10],[512, 859],[494, 362],[-955, -475],[128, 553],[-986, -885],[763, 77],[449, 310]])
    7641.9817824387
    """
    fac = math.factorial(N)
    perm_list = list(itertools.permutations(range(N) ) )
    table = distance(N, ar)
    dist = 0
    for perm in perm_list:
        for i in range(len(perm) -1):
            dist += table[perm[i]][perm[i+1]]
    print(dist/fac)


if __name__ == '__main__':
    N = int(input().rstrip())
    ar = [list(map(int, input().rstrip().split())) for _ in range(N)]
    print_ans(N, ar)

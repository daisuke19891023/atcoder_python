import sys
input = sys.stdin.readline
import heapq as hq
def print_ans(N, M, input_line):
    """Test Case
    >>> print_ans(3, 3, "2 13 8")
    9
    >>> print_ans(4, 4, "1 9 3 5")
    6
    >>> print_ans(1, 100000, "1000000000")
    0
    >>> print_ans(10 ,1, "1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000")
    9500000000
    """
    ar = [-int(i) for i in input_line.split()]
    hq.heapify(ar)
    for _ in range(M):
        hq.heappush(ar, -(-hq.heappop(ar) // 2))
    
    print(-sum(ar))

if __name__ == '__main__':
    N, M = map(int, input().rstrip().split())
    input_line = input().rstrip()
    print_ans(N, M, input_line)

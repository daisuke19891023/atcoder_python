import sys
input = sys.stdin.readline
def primes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]
def print_ans(X):
    """Test Case
    >>> print_ans(20)
    23
    >>> print_ans(2)
    2
    >>> print_ans(99992)
    100003
    """
    ord = 10 ** 6
    prime_list = primes(ord)
    for i in prime_list:
        if i >= X:
            print(i)
            break
if __name__ == '__main__':
    # test
    X = int(input().rstrip())
    print_ans(X)
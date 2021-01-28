import sys
read = sys.stdin.readline

n, r = map(int, read().split())
dp = [0] * (n + 1)
dp[0], dp[1] = 1, 1


def factorial(n):
    if dp[n] == 0:
        return n * factorial(n - 1)
    else:
        return dp[n]


print(factorial(n) // (factorial(r) * factorial(n - r)))

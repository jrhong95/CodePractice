import sys

read = sys.stdin.readline
dp = [[0] * 31 for _ in range(31)]


def combination(n, r):
    if dp[n][r] == 0:
        if n == r or r == 0:
            dp[n][r] = 1
        else:
            dp[n][r] = combination(n - 1, r - 1) + combination(n - 1, r)

    return dp[n][r]


def main():
    for _ in range(int(read())):
        N, M = map(int, read().split())
        print(combination(M, N))


main()
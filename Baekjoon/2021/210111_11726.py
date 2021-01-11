import sys
read = sys.stdin.readline

N = int(read())

dp = []
dp.append(1)
dp.append(2)

for i in range(2, N):
    dp.append(dp[i - 1] + dp[i - 2])

print(dp[N - 1] % 10007)

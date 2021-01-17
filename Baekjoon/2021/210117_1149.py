import sys
read = sys.stdin.readline

N = int(read())
tmp = list(map(int, read().split()))
houses, dp = [], []
houses.append(tmp)
dp.append(tmp)

for i in range(1, N):
    houses.append(list(map(int, read().split())))
    tmp = []
    tmp.append(min(houses[i][0] + dp[i - 1][1], houses[i][0] + dp[i - 1][2]))
    tmp.append(min(houses[i][1] + dp[i - 1][0], houses[i][1] + dp[i - 1][2]))
    tmp.append(min(houses[i][2] + dp[i - 1][0], houses[i][2] + dp[i - 1][1]))

    dp.append(tmp)

print(min(dp[N - 1]))

import sys

read = sys.stdin.readline

N, M = map(int, read().split())
mems = list(map(int, read().split()))
costs = list(map(int, read().split()))
ans = 0

cost_sum = sum(costs) + 1
dp = [[0] * cost_sum for _ in range(N)]

for i in range(N):
    for j in range(cost_sum):
        if j - costs[i] >= 0:
            dp[i][j] = dp[i - 1][j - costs[i]] + mems[i]
        dp[i][j] = max(dp[i - 1][j], dp[i][j])

for i, c in enumerate(dp[N - 1]):
    if M <= c:
        ans = i
        break

print(ans)

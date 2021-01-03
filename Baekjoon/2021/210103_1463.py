n = int(input())
cnt = 0

dp = [0, 0, 1, 1]
for i in range(4, n + 1):
    dp.append(dp[i - 1] + 1)
    for j in [2, 3]:
        if i % j == 0:
            dp[i] = min(dp[i // j] + 1, dp[i])
print(dp[n])
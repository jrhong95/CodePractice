import sys

read = sys.stdin.readline

s1 = read().rstrip()
s2 = read().rstrip()
dp = [[0] * (len(s1) + 1) for _ in range(len(s2) + 1)]

ans = 0
for i in range(1, len(s2) + 1):
    for j in range(1, len(s1) + 1):
        if s1[j - 1] == s2[i - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        ans = max(ans, dp[i][j])

print(ans)
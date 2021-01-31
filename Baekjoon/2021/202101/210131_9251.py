import sys
read = sys.stdin.readline

s1 = read().rstrip()
s2 = read().rstrip()
dp = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
answer = 0

for i in range(1, len(s1) + 1):
    for j in range(1, len(s2) + 1):
        dp[i][j] = dp[i - 1][j - 1] + 1 if s1[i - 1] == s2[j - 1]\
            else max(dp[i - 1][j], dp[i][j - 1])
        answer = max(answer, dp[i][j])

print(answer)

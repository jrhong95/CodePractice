import sys

read = sys.stdin.readline

s1 = read().rstrip()
len1 = len(s1)
s2 = read().rstrip()
len2 = len(s2)
dp = [[0] * (len1 + 1) for _ in range(len2 + 1)]

for i in range(1, len2 + 1):
    for j in range(1, len1 + 1):
        if s1[j - 1] == s2[i - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[len2][len1])
if dp[len2][len1] != 0:
    stack = []
    while len1 != 0 and len2 != 0:
        if s1[len1 - 1] == s2[len2 - 1]:
            stack.append(s1[len1 - 1])
            len1 -= 1
            len2 -= 1
        elif dp[len2][len1] == dp[len2 - 1][len1]:
            len2 -= 1
        elif dp[len2][len1] == dp[len2][len1 - 1]:
            len1 -= 1

    print("".join(stack[::-1]))

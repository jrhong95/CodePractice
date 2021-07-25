import sys

read = sys.stdin.readline

N = int(read())
nums = list(map(int, read().split()))
dp = [[0] * 21 for _ in range(N - 1)]

dp[0][nums.pop(0)] = 1
goal = nums.pop(-1)

for i, n in enumerate(nums):
    for j in range(21):
        if dp[i][j] > 0:
            if j + n <= 20:
                dp[i + 1][j + n] += dp[i][j]
            if j - n >= 0:
                dp[i + 1][j - n] += dp[i][j]

print(dp[-1][goal])
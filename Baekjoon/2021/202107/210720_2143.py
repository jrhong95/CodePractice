N = int(input())
if N == 0:
    print(0)
elif N == 1 or N == 2:
    print(1)
else:
    dp = [0] * (N + 1)
    dp[1], dp[2] = 1, 1

    for i in range(3, N + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    print(dp[-1])
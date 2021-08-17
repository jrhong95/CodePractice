import sys

read = sys.stdin.readline

N = int(read())
nums = list(map(int, read().split()))
M = int(read())

dp = [[""] * (M + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for w in range(1, M + 1):
        if w < nums[i - 1]:
            pass
        else:
            dup = w // nums[i - 1]
            rest = w % nums[i - 1]
            tmp = f"{i - 1}" * dup
            # print(tmp + dp[i - 1][rest])
            # print()
            # dp[i][w] = max(int(tmp + dp[i - 1][rest]), int(dp[i - 1][w]))

            if dp[i - 1][w] != "":
                tmp = tmp + dp[i - 1][rest]
                dp[i][w] = max(int(tmp), int(dp[i - 1][w]))
                dp[i][w] = str(dp[i][w])
            else:
                dp[i][w] = tmp + dp[i - 1][rest]


print(dp)
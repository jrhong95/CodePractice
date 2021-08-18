import sys

read = sys.stdin.readline

N = int(read())
nums = list(map(int, read().split()))
M = int(read())

dp = [[""] * (M + 1) for _ in range(N + 1)]
zero_dp = ["" for _ in range(M + 1)]

for w in range(1, M + 1):
    if nums[0] <= w:
        zero_dp[w] = "0" * (w // nums[0])

for i in range(1, N + 1):
    for w in range(1, M + 1):
        if w < nums[i - 1]:
            dp[i][w] = dp[i - 1][w]
        else:
            dup = 1
            while dup * nums[i - 1] <= w:
                rest = w - (dup * nums[i - 1])
                tmp = f"{i - 1}" * dup

                if dp[i - 1][w] != "":
                    tmp_max = max(int(tmp + dp[i - 1][rest]), int(dp[i - 1][w]))
                    if dp[i][w] != "":
                        tmp_max = max(tmp_max, int(dp[i][w]))
                    dp[i][w] = str(tmp_max)
                else:
                    dp[i][w] = tmp + dp[i - 1][rest]

                if zero_dp[rest] != "":
                    dp[i][w] = str(max(int(dp[i][w]), int(tmp + zero_dp[rest])))
                dup += 1

print(int(dp[-1][-1]))
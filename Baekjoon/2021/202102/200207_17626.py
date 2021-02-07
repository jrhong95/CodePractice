import sys
read = sys.stdin.readline

N = int(read())
dp = [0, 1]

n = 2
for i in range(2, N + 1):
    if n ** 2 == i:
        dp.append(1)
        n += 1
    else:
        min_val = sys.maxsize
        tmp = 1

        while (tmp ** 2) < i:
            min_val = min(min_val, dp[i - (tmp ** 2)])
            tmp += 1
        dp.append(min_val + 1)

print(dp[-1])

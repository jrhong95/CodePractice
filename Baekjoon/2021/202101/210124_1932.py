import sys
read = sys.stdin.readline

N = int(read())
dp = [int(read())]

for i in range(1, N):
    tmp = []
    line = list(map(int, read().split()))
    for j, n in enumerate(line):
        if j == 0:
            tmp.append(dp[0] + n)
        elif j == len(line) - 1:
            tmp.append(dp[-1] + n)
        else:
            tmp.append(max(dp[j - 1] + n, dp[j] + n))
    dp = tmp

print(max(dp))

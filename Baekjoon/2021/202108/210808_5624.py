import sys

read = sys.stdin.readline

MID = 200000

N = int(read())
nums = list(map(int, read().split()))

check_sum = [False] * (MID * 2 + 1)

cnt = 0

for i in range(N):
    for j in range(i):
        if check_sum[nums[i] - nums[j] + MID]:
            cnt += 1
            break

    for j in range(i + 1):
        check_sum[nums[i] + nums[j] + MID] = True

print(cnt)
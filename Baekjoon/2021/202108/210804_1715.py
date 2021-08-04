import sys
from heapq import *

read = sys.stdin.readline

nums = sorted([int(read()) for _ in range(int(read()))])

ans = 0
while len(nums) > 1:
    cur_sum = heappop(nums) + heappop(nums)
    ans += cur_sum
    heappush(nums, cur_sum)
print(ans)

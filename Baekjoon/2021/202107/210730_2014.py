import sys
from heapq import *

read = sys.stdin.readline

K, N = map(int, read().split())
nums = list(map(int, read().split()))

heap = nums[:]

cur = 0
for i in range(N):
    cur = heappop(heap)
    for n in nums:
        heappush(heap, cur * n)
        if cur % n == 0:
            break

print(cur)

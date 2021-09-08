import sys
from heapq import *


read = sys.stdin.readline

N, M = map(int, read().split())
indegree = [0] * (N + 1)
adjust = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, read().split())
    indegree[b] += 1
    adjust[a].append(b)

heap = []
for i in range(1, N + 1):
    if indegree[i] == 0:
        heappush(heap, i)

ans = []
while heap:
    cur = heappop(heap)
    ans.append(cur)
    for n in adjust[cur]:
        indegree[n] -= 1
        if indegree[n] == 0:
            heappush(heap, n)

print(*ans, sep=" ")

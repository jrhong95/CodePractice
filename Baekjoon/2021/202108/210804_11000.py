import sys
from heapq import *
from collections import deque


read = sys.stdin.readline

N = int(read())
times = deque(sorted([list(map(int, read().split())) for _ in range(N)]))
heap = []
s, e = times.popleft()
heappush(heap, (e, s))
count = 1

while times:
    start, end = times.popleft()

    if heap[0][0] <= start:  # 강의의 종료시간보다 새로 들어온 강의의 시작시간이 큰 경우
        heappop(heap)
    else:
        count += 1
    heappush(heap, (end, start))

print(count)
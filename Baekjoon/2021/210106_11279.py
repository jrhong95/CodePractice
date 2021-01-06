from heapq import heappop, heappush
import sys
read = sys.stdin.readline

heap = []
for _ in range(int(read())):
    n = int(read())

    if n == 0:
        print(-heappop(heap) if heap else 0)
    else:
        heappush(heap, -n)
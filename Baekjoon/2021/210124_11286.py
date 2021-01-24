import sys
from heapq import heappush, heappop
read = sys.stdin.readline

heap = []
for _ in range(int(read())):
    n = int(read())
    if n != 0:
        heappush(heap, (abs(n), n))
    else:
        print(heappop(heap)[1] if heap else 0)

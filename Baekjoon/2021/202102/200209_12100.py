import sys
import heapq
read = sys.stdin.readline

N = int(read())
min_heap, max_heap = [], []
for i in range(1, N + 1):
    if i % 2:
        heapq.heappush(max_heap, -int(read()))
    else:
        heapq.heappush(min_heap, int(read()))

    if min_heap and -max_heap[0] > min_heap[0]:
        max_heap_val = -heapq.heappop(max_heap)
        min_heap_val = heapq.heappop(min_heap)
        heapq.heappush(max_heap, -min_heap_val)
        heapq.heappush(min_heap, max_heap_val)

    print(-max_heap[0])

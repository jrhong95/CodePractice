import sys
from heapq import heappop, heappush

input = sys.stdin.readline

for _ in range(int(input())):
    max_heap, min_heap = [], []
    del_max_heap, del_min_heap = [], []

    for _ in range(int(input())):
        c, n = input().split()
        n = int(n)

        if c == "I":
            heappush(min_heap, n)
            heappush(max_heap, -n)

        else:
            if n == 1:
                if max_heap:
                    heappush(del_max_heap, -heappop(max_heap))
            else:
                if min_heap:
                    heappush(del_min_heap, -heappop(min_heap))

        while max_heap and del_min_heap and max_heap[0] == del_min_heap[0]:
            heappop(max_heap)
            heappop(del_min_heap)

        while min_heap and del_max_heap and min_heap[0] == del_max_heap[0]:
            heappop(min_heap)
            heappop(del_max_heap)

    if not max_heap:
        print("EMPTY")

    else:
        print(-max_heap[0], min_heap[0])
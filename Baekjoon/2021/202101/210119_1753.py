import sys
from collections import defaultdict
from heapq import heappop, heappush
read = sys.stdin.readline

INF = 10 * 300000
V, E = map(int, read().split())
start = int(read())

graph = [dict() for _ in range(V + 1)]
distance = [INF for _ in range(V + 1)]


def dijkstra(start):
    heap = []
    heappush(heap, (0, start))

    while heap:
        dist, child = heappop(heap)

        if distance[child] >= dist:
            for v, w in graph[child].items():
                w += dist
                if w < distance[v]:
                    distance[v] = w
                    heappush(heap, (w, v))


for _ in range(E):
    u, v, w = map(int, read().split())
    if v in graph[u]:
        graph[u][v] = min(w, graph[u][v])
    else:
        graph[u][v] = w

distance[start] = 0
dijkstra(start)

for i in range(1, V + 1):
    print("INF" if distance[i] == INF else distance[i])

import sys
import heapq
read = sys.stdin.readline
INF = sys.maxsize

N, M, X = map(int, read().split())
graph1 = [dict() for _ in range(N + 1)]
graph2 = [dict() for _ in range(N + 1)]
distance1 = [INF for _ in range(N + 1)]
distance2 = [INF for _ in range(N + 1)]


def dijkstra(start, graph, distance):
    heap = []
    heapq.heappush(heap, (0, start))

    while heap:
        dist, child = heapq.heappop(heap)

        if distance[child] >= dist:
            for v, w in graph[child].items():
                w += dist
                if w < distance[v]:
                    distance[v] = w
                    heapq.heappush(heap, (w, v))


for _ in range(M):
    u, v, w = map(int, read().split())
    if v in graph1[u]:
        graph1[u][v] = min(w, graph1[u][v])
    else:
        graph1[u][v] = w

    if u in graph2[v]:
        graph2[v][u] = min(w, graph2[v][u])
    else:
        graph2[v][u] = w

distance1[X], distance2[X] = 0, 0
dijkstra(X, graph1, distance1)
dijkstra(X, graph2, distance2)

ans = max(distance1[i] + distance2[i] for i in range(1, N + 1))
print(ans)

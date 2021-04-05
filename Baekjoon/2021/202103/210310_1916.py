import heapq
import sys
read = sys.stdin.readline
INF = sys.maxsize

N = int(read())
graph = [[INF] * (N + 1) for _ in range(N + 1)]


def dijkstra(start):
    distance = [INF] * (N + 1)
    heap = []
    heapq.heappush(heap, (0, start))
    distance[start] = 0
    while heap:
        cur_dist, cur_node = heapq.heappop(heap)

        if cur_dist > distance[cur_node]:
            continue

        for next_node in range(1, N + 1):
            next_dist = graph[cur_node][next_node]
            if next_dist + cur_dist < distance[next_node]:
                distance[next_node] = next_dist + cur_dist
                heapq.heappush(heap, (distance[next_node], next_node))

    return distance


for _ in range(int(read())):
    u, v, w = map(int, read().split())
    graph[u][v] = min(w, graph[u][v])

start, end = map(int, read().split())
print(dijkstra(start)[end])

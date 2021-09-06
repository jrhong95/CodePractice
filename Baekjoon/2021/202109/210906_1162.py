import sys
from heapq import *

INF = sys.maxsize
read = sys.stdin.readline

N, M, K = map(int, read().split())
road = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, read().split())
    road[a].append((b, c))
    road[b].append((a, c))


def dijkstra():
    heap = []
    dist = [[INF] * (K + 1) for _ in range(N + 1)]
    dist[1] = [0] * (K + 1)
    heappush(heap, (0, 1, 0))  # cost, 현재 노드, 포장횟수

    while heap:
        total_cost, cur_node, pojang = heappop(heap)

        if total_cost > dist[cur_node][pojang]:
            continue
        for next_node, cost in road[cur_node]:
            if dist[next_node][pojang] > dist[cur_node][pojang] + cost:
                dist[next_node][pojang] = dist[cur_node][pojang] + cost
                heappush(heap, (dist[next_node][pojang], next_node, pojang))
            if pojang < K and dist[next_node][pojang + 1] > dist[cur_node][pojang]:
                dist[next_node][pojang + 1] = dist[cur_node][pojang]
                heappush(heap, (dist[next_node][pojang + 1], next_node, pojang + 1))

    return min(dist[-1])


print(dijkstra())
import sys
import heapq
from collections import deque

read = sys.stdin.readline
INF = sys.maxsize

N, P, K = map(int, read().split())
graph = [[] for _ in range(N + 1)]


def main():
    right = 0
    for _ in range(P):
        v1, v2, d = map(int, read().split())
        graph[v1].append((v2, d))
        graph[v2].append((v1, d))
        right = max(d, right)

    left, mid, ans = 0, 0, -1
    while left <= right:
        mid = (left + right) // 2

        if dijkstra(mid):
            ans = mid
            right = mid - 1
        else:
            left = mid + 1

    print(ans)


def dijkstra(target):
    dist = [INF] * (N + 1)
    dist[1] = 0
    pq = []
    heapq.heappush(pq, (0, 1))

    while pq:
        cost, cur = heapq.heappop(pq)
        if dist[cur] < cost:
            continue
        for nxt, nxt_cost in graph[cur]:
            nxt_cost = cost + (nxt_cost > target)

            if dist[nxt] > nxt_cost:
                dist[nxt] = nxt_cost
                heapq.heappush(pq, (nxt_cost, nxt))

    return dist[N] <= K


main()

import sys
import heapq
read = sys.stdin.readline
INF = sys.maxsize

N, E = map(int, read().split())


def dijkstra(start, graph):
    heap = []
    heapq.heappush(heap, (0, start))

    distance = [INF for _ in range(N + 1)]
    distance[start] = 0

    while heap:
        cur_dist, cur_node = heapq.heappop(heap)
        if distance[cur_node] < cur_dist:
            continue

        for next_node in range(1, N + 1):
            next_dist = graph[cur_node][next_node]

            if next_dist != 0:
                dist = cur_dist + next_dist

                if dist < distance[next_node]:
                    distance[next_node] = dist
                    heapq.heappush(heap, (dist, next_node))

    return distance


def solve():
    graph = [[0] * (N + 1) for _ in range(N + 1)]

    for _ in range(E):
        n, v, w = map(int, read().split())
        graph[n][v] = w
        graph[v][n] = w

    a, b = map(int, read().split())

    dist1 = dijkstra(1, graph)
    dist2 = dijkstra(a, graph)
    dist3 = dijkstra(b, graph)

    res1 = dist1[a] + dist2[b] + dist3[N]
    res2 = dist1[b] + dist3[a] + dist2[N]

    if res1 >= INF and res2 >= INF:
        print(-1)
        return
    else:
        print(min(res1, res2))


solve()

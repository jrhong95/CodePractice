import sys
from collections import deque, defaultdict
read = sys.stdin.readline
INF = sys.maxsize


def bf():
    dist = [INF] * (N + 1)
    dist[1] = 0
    updated = False

    for count in range(N):
        updated = False
        for node in graph:
            for v, w in graph[node]:
                if dist[v] > dist[node] + w:
                    dist[v] = dist[node] + w
                    updated = True

        if not updated:
            return False

    return True if updated else False


for _ in range(int(read())):
    graph = defaultdict(list)
    N, M, W = map(int, read().split())

    for _ in range(M):
        s, e, t = map(int, read().split())
        graph[s].append((e, t))
        graph[e].append((s, t))

    for _ in range(W):
        s, e, t = map(int, read().split())
        graph[s].append((e, -t))

    print("YES" if bf() else "NO")

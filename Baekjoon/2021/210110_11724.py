import sys
from collections import deque
read = sys.stdin.readline

N, M = map(int, read().split())
graph = [[False] * (N + 1) for _ in range(N + 1)]
not_visited = set()


def bfs():
    queue = deque()

    connected = 0

    while not_visited:
        queue.append(not_visited.pop())

        while queue:
            node = queue.popleft()

            for i in range(1, N + 1):
                if graph[node][i] and i in not_visited:
                    queue.append(i)
                    not_visited.remove(i)

        connected += 1

    print(connected)


for _ in range(M):
    u, v = map(int, read().split())
    graph[u][v] = True
    graph[v][u] = True
    not_visited.add(u)
    not_visited.add(v)

bfs()

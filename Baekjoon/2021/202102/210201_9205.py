import sys
from collections import deque
read = sys.stdin.readline


def bfs():
    visited = [False] * (cvs + 2)
    queue = deque([0])
    visited[0] = True
    while queue:
        n = queue.popleft()
        if n == cvs + 1:
            return "happy"

        for i, c in enumerate(graph[n]):
            if not visited[i] and c == 1:
                queue.append(i)
                visited[i] = True

    return "sad"


for _ in range(int(read())):
    cvs = int(read())
    nodes = [tuple(map(int, read().split())) for _ in range(cvs + 2)]
    graph = [[0] * (cvs + 2) for _ in range(cvs + 2)]

    for i in range(cvs + 2):
        x, y = nodes[i]
        for j in range(cvs + 2):
            z, w = nodes[j]
            if abs(x - z) + abs(y - w) <= 1000:
                graph[i][j] = 1

    print(bfs())

import sys
from collections import defaultdict, deque

read = sys.stdin.readline


def bfs(start, minimum):
    visited = [False] * (N + 1)
    visited[start] = True
    queue = deque([start])
    count = 0

    while queue:
        video = queue.popleft()

        for q, r in graph[video]:
            if not visited[q] and r >= minimum:
                visited[q] = True
                queue.append(q)
                count += 1

    return count


N, Q = map(int, read().split())
graph = defaultdict(list)

for _ in range(N - 1):
    p, q, r = map(int, read().split())

    graph[p].append((q, r))
    graph[q].append((p, r))


for _ in range(Q):
    k, v = map(int, read().split())
    print(bfs(v, k))
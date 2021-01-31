import sys
from collections import deque
read = sys.stdin.readline


def bfs():
    queue = deque([1])
    count = 0
    while queue:
        node = queue.popleft()

        for i in range(N + 1):
            if graph[node][i] and not visit[i]:
                count += 1
                queue.append(i)
                visit[i] = True
    
    print(count)
    



N = int(read())
graph = [[False] * (N + 1) for _ in range(N + 1)]
visit = [False for _ in range(N + 1)]
visit[1] = True

for _ in range(int(read())):
    x, y = map(int, read().split())
    graph[x][y] = True
    graph[y][x] = True

bfs()

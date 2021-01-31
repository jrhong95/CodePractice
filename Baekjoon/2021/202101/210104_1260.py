from collections import defaultdict, deque


def dfs(graph, start):
    print(start, end=' ')
    visit.append(start)

    for i in range(1, N + 1):
        if graph[start][i] == 1 and i not in visit:
            dfs(graph, i)
    

def bfs(gragh, start):
    queue = deque()
    queue.append(start)

    while queue:
        node = queue.popleft()

        if node not in visit:
            visit.append(node)
            print(node, end=' ')
            for i in range(1, N + 1):
                if graph[node][i] == 1 and i not in visit:
                    queue.append(i)


N, M, V = map(int, input().split())
graph = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    x, y = map(int, input().split())
    graph[y][x] = 1
    graph[x][y] = 1

visit = []
dfs(graph, V)
print()
visit = []
bfs(graph, V)

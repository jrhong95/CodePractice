from collections import deque


def bfs(start):
    queue = deque()
    visit = []
    queue.append((start, 0))
    link = 0
    while queue:
        node = queue.popleft()
        if node[0] not in visit:
            link += node[1]
            visit.append(node[0])
            for i in range(1, N + 1):
                if graph[node[0]][i] == 1 and i not in visit:
                    queue.append((i, node[1] + 1))
    return link


N, M = map(int, input().split())

friends = set()
graph = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    x, y = map(int, input().split())
    friends.add(x)
    friends.add(y)
    graph[x][y] = 1
    graph[y][x] = 1

dic = dict()
for friend in friends: 
    dic[friend] = bfs(friend) 
dic = sorted(dic.items(), key=lambda x: x[1])
print(dic[0][0])


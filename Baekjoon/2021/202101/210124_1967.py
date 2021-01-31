import sys
from collections import deque, defaultdict
read = sys.stdin.readline


N = int(read())
tree = defaultdict(list)


def bfs(start):
    max_dist = 0
    max_node = start
    queue = deque()
    visited = [False] * (N + 1)
    queue.append((start, 0))
    visited[start] = True

    while queue:
        node, dist = queue.popleft()
        if max_dist < dist:
            max_dist = dist
            max_node = node

        subnode_list = tree[node]

        for subnode, weight in subnode_list:
            if not visited[subnode]:
                visited[subnode] = True
                queue.append((subnode, dist + weight))

    return max_node, max_dist


for _ in range(N - 1):
    u, v, w = map(int, read().split())
    tree[u].append((v, w))
    tree[v].append((u, w))


max_node, max_dist = bfs(1)
max_node, max_dist = bfs(max_node)
print(max_dist)

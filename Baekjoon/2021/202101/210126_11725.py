import sys
from collections import deque, defaultdict
read = sys.stdin.readline

N = int(read())

tree = defaultdict(list)
parent = [0 for _ in range(N + 1)]

for _ in range(N - 1):
    u, v = map(int, read().split())
    tree[u].append(v)
    tree[v].append(u)

queue = deque([1])
while queue:
    node = queue.popleft()
    leafs = tree[node]
    for leaf in leafs:
        if parent[leaf] == 0:
            parent[leaf] = node
            queue.append(leaf)

for i in range(2, N + 1):
    print(parent[i])

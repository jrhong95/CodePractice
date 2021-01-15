import sys
from collections import deque, defaultdict
read = sys.stdin.readline
max_len = 0
max_node = 0


def dfs(start, length):
    global max_len, max_node

    if max_len < length:
        max_len = length
        max_node = start

    for node in tree[start]:
        n, l = node
        if not visited[n]:
            visited[n] = True
            dfs(n, length + l)
            visited[n] = False


N = int(read())
tree = defaultdict(list)

for _ in range(N):
    nums = list(map(int, read().split()))

    for i in range(1, len(nums) - 1, 2):
        tree[nums[0]].append((nums[i], nums[i + 1]))

visited = [False for _ in range(N + 1)]
visited[1] = True
dfs(1, 0)

visited = [False for _ in range(N + 1)]
visited[max_node] = True
dfs(max_node, 0)

print(max_len)

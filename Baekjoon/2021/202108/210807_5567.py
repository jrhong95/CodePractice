import sys
from collections import deque

read = sys.stdin.readline

N = int(read())
graph = [[] for _ in range(N + 1)]

for _ in range(int(read())):
    a, b = map(int, read().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs():
    queue = deque()
    queue.append((1, 0))
    checked = [False] * (N + 1)
    checked[1] = True

    while queue:
        node, depth = queue.popleft()

        if depth == 2:
            continue
        for next_node in graph[node]:
            if not checked[next_node]:
                checked[next_node] = True
                queue.append((next_node, depth + 1))

    return sum(checked) - 1


def main():
    print(bfs())


main()
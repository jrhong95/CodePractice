import sys
from collections import deque

read = sys.stdin.readline


def is_tree(n):
    flag = True
    queue = deque()
    queue.append(n)

    while queue:
        cur = queue.popleft()
        if visited[cur]:
            flag = False
        visited[cur] = True
        for nxt in tree[cur]:
            if not visited[nxt]:
                queue.append(nxt)

    return flag


def main():
    global tree, visited
    tc = 1

    while True:
        N, M = map(int, read().split())
        if N == 0 and M == 0:
            break
        tree = [[] for _ in range(N + 1)]
        visited = [False] * (N + 1)

        for _ in range(M):
            a, b = map(int, read().split())
            tree[a].append(b)
            tree[b].append(a)

        cnt = sum(is_tree(i) for i in range(1, N + 1) if not visited[i])

        if cnt >= 2:
            print(f"Case {tc}: A forest of {cnt} trees.")
        elif cnt == 1:
            print(f"Case {tc}: There is one tree.")
        else:
            print(f"Case {tc}: No trees.")
        tc += 1


main()

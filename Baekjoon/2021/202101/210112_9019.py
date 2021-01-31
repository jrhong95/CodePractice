import sys
from collections import deque
read = sys.stdin.readline


def bfs(start, end):
    visit = [False for _ in range(10000)]
    queue = deque()
    queue.append((start, ""))
    visit[start] = True

    while queue:
        num, trace = queue.popleft()

        if num == end:
            print(trace)
            return

        # D
        tmp = num * 2 % 10000
        if not visit[tmp]:
            visit[tmp] = True
            queue.append((tmp, trace + 'D'))

        # S
        tmp = num - 1 if num > 0 else 9999
        if not visit[tmp]:
            visit[tmp] = True
            queue.append((tmp, trace + 'S'))

        # L
        tmp = num % 1000 * 10 + num // 1000
        if not visit[tmp]:
            visit[tmp] = True
            queue.append((tmp, trace + 'L'))

        # R
        tmp = num % 10 * 1000 + num // 10
        if not visit[tmp]:
            visit[tmp] = True
            queue.append((tmp, trace + 'R'))


for _ in range(int(read())):
    A, B = map(int, read().split())
    bfs(A, B)

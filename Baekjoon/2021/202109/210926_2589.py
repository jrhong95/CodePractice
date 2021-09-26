import sys
from collections import deque

read = sys.stdin.readline

R, C = map(int, read().split())
board = [list(read().rstrip()) for _ in range(R)]

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]


def bfs(r, c):
    visited = [[False] * C for _ in range(R)]
    visited[r][c] = True
    queue = deque([(r, c, 0)])
    max_time = 0

    while queue:
        cr, cc, count = queue.popleft()
        max_time = max(max_time, count)

        for i in range(4):
            nr, nc = cr + dr[i], cc + dc[i]
            if (
                not 0 <= nr < R
                or not 0 <= nc < C
                or board[nr][nc] == "W"
                or visited[nr][nc]
            ):
                continue
            queue.append((nr, nc, count + 1))
            visited[nr][nc] = True

    return max_time


def main():
    max_time = 0
    for i in range(R):
        for j in range(C):
            if board[i][j] != "W":
                max_time = max(max_time, bfs(i, j))
    print(max_time)


main()
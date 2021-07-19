import sys
from collections import deque

read = sys.stdin.readline

move = [(0, 1), (0, -1), (1, 0), (-1, 0)]

R, C = map(int, read().split())
matrix = [list(read().rstrip()) for _ in range(R)]
visited = [[0] * C for _ in range(R)]
water_pos = []

goal, start = 0, 0
for i in range(R):
    for j in range(C):
        if matrix[i][j] == "D":
            goal = (i, j)
        if matrix[i][j] == "S":
            start = (i, j)
            visited[i][j] = 0
        if matrix[i][j] == "*":
            water_pos.append((i, j, "*"))

# BFS
def bfs():
    queue = deque(water_pos)
    queue.append((start[0], start[1], "S"))

    while queue:
        r, c, tp = queue.popleft()

        # 물
        if tp == "*":
            for mr, mc in move:
                nr, nc = r + mr, c + mc
                if (
                    0 <= nr < R
                    and 0 <= nc < C
                    and matrix[nr][nc] != "X"
                    and matrix[nr][nc] != "D"
                    and matrix[nr][nc] != "*"
                ):
                    matrix[nr][nc] = "*"
                    queue.append((nr, nc, "*"))

        # 고슴도치
        else:
            if r == goal[0] and c == goal[1]:
                return visited[r][c]
            for mr, mc in move:
                nr, nc = mr + r, mc + c
                if (
                    0 <= nr < R
                    and 0 <= nc < C
                    and matrix[nr][nc] != "X"
                    and matrix[nr][nc] != "*"
                    and visited[nr][nc] == 0
                ):
                    queue.append((nr, nc, "S"))
                    visited[nr][nc] = visited[r][c] + 1

    return "KAKTUS"


print(bfs())

import sys
from collections import deque
read = sys.stdin.readline

R, C = map(int, read().split())
board = [list(map(str, list(read().rstrip()))) for _ in range(R)]
visited = [[[0] * 2 for _ in range(C)] for _ in range(R)]


def bfs():
    queue = deque()
    queue.append((0, 0, 1))
    visited[0][0][1] = 1

    while queue:
        r, c, wall = queue.popleft()

        if r == R - 1 and c == C - 1:
            return visited[r][c][wall]

        for move in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            move_r, move_c = r + move[0], c + move[1]

            if 0 <= move_r < R and 0 <= move_c < C:
                if board[move_r][move_c] == '1' and wall == 1:
                    queue.append((move_r, move_c, 0))
                    visited[move_r][move_c][0] = visited[r][c][1] + 1
                elif board[move_r][move_c] == '0' and visited[move_r][move_c][wall] == 0:
                    queue.append((move_r, move_c, wall))
                    visited[move_r][move_c][wall] = visited[r][c][wall] + 1

    return -1


print(bfs())

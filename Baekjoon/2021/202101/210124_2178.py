import sys
from collections import deque
read = sys.stdin.readline

R, C = map(int, read().split())
board = [list(map(int, list(read().rstrip()))) for _ in range(R)]


def bfs(end):
    queue = deque()
    queue.append(((0, 0), 1))

    visited = [[False] * C for _ in range(R)]
    visited[0][0] = True
    min_count = sys.maxsize

    while queue:
        node, count = queue.popleft()
        min_count = min(min_count, count)

        for move in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            move_r, move_c = node[0] + move[0], node[1] + move[1]

            if 0 <= move_r < R and 0 <= move_c < C and board[move_r][move_c] != 0 and not visited[move_r][move_c]:
                visited[move_r][move_c] = True
                if move_r == end[0] and move_c == end[1]:
                    print(count + 1)
                    break
                else:
                    queue.append(((move_r, move_c), count + 1))


bfs((R - 1, C - 1))

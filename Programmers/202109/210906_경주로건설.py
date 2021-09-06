from collections import deque

STRGHT, CORNER, INF = 100, 600, 10 ** 9
dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]


def solution(board):
    N = len(board)
    visited = [[[INF] * 4 for __ in range(N)] for _ in range(N)]
    for i in range(4):
        visited[0][0][i] = 0

    queue = deque()
    queue.append((0, 0, -1))  # r, c, previous_direction

    while queue:
        r, c, prev_dir = queue.popleft()
        if r == N - 1 and c == N - 1:
            continue

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if not 0 <= nr < N or not 0 <= nc < N or board[nr][nc] == 1:
                continue

            if prev_dir == -1 or prev_dir == i:  # 처음 or 이전 방향과 같을 때
                if visited[r][c][prev_dir] + STRGHT <= visited[nr][nc][i]:
                    queue.append((nr, nc, i))
                    visited[nr][nc][i] = visited[r][c][prev_dir] + STRGHT
            else:
                if visited[r][c][prev_dir] + CORNER <= visited[nr][nc][i]:
                    queue.append((nr, nc, i))
                    visited[nr][nc][i] = visited[r][c][prev_dir] + CORNER

    return min(visited[N - 1][N - 1])


board = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 1, 0, 0],
    [1, 0, 0, 0, 1],
    [0, 1, 1, 0, 0],
]

print(solution(board))
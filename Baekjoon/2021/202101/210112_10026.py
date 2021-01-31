import sys
from collections import deque
read = sys.stdin.readline

count = []


def pop_color(color):
    global visited
    for i in range(N):
        for j in range(N):
            if color_map[i][j] in color and visited[i][j] == 0:
                return (j, i)
    return None


def bfs():
    queue = deque()
    global visited
    for color in ['B', 'RG', 'R', 'G']:
        visited = [[0] * N for _ in range(N)]
        color_point = pop_color(color)
        color_count = 0

        while color_point is not None:
            queue.append(color_point)
            visited[color_point[1]][color_point[0]] = 1
            color_count += 1

            while queue:
                x, y = queue.popleft()

                for point in [(0, -1), (0, 1), (-1, 0), (1, 0)]:  # U, D, L, R
                    move_x, move_y = x + point[0], y + point[1]
                    if 0 <= move_x < N and 0 <= move_y < N and \
                            visited[move_y][move_x] == 0 and color_map[move_y][move_x] in color:
                        visited[move_y][move_x] = 1
                        queue.append((move_x, move_y))

            color_point = pop_color(color)

        count.append(color_count)
    print(f'{count[0] + count[2] + count[3]} {count[0] + count[1]}')


N = int(read())
color_map = [list(read().rstrip()) for _ in range(N)]
visited = []
bfs()

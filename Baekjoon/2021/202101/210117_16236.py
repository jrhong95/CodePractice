import sys
from collections import deque
read = sys.stdin.readline
size = 2


def bfs(start):
    queue = deque([(start, 0)])
    visited = [[False] * N for _ in range(N)]
    visited[start[0]][start[1]] = True
    can_eat = []

    while queue:
        point, dist = queue.popleft()
        r, c = point

        for move in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            move_r, move_c = move[0] + r, move[1] + c

            if 0 <= move_r < N and 0 <= move_c < N and not visited[move_r][move_c] and board[move_r][move_c] <= size:
                visited[move_r][move_c] = True

                if 0 < board[move_r][move_c] < size:
                    can_eat.append((move_r, move_c, dist + 1))
                else:
                    queue.append(((move_r, move_c), dist + 1))

    if can_eat:
        can_eat.sort(key=lambda x: (x[2], x[0], x[1]))
        eat = can_eat[0]
        board[start[0]][start[1]] = 0
        board[eat[0]][eat[1]] = 9
        return (eat[0], eat[1]), eat[2]
    else:
        return None, -1


"""
1.  bfs로 먹을 수 있는 먹을 수 있는 물고기 탐색, 없을 때 break
2.  먹을 수 있는 물고기 중 조건에 맞는 최단거리 물고기로 이동
3.  다시 bfs
"""
N = int(read())
board = []
start = tuple()
for i in range(N):
    line = list(map(int, read().split()))
    for j in range(len(line)):
        if line[j] == 9:
            start = (i, j)
    board.append(line)

exp = 0
dist = 0

while True:
    point, move = bfs(start)

    if point is None:
        break

    exp += 1
    if exp == size:
        size += 1
        exp = 0
    dist += move
    start = point

print(dist)

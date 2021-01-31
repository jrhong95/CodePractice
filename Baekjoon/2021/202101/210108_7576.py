import sys
from collections import deque
read = sys.stdin.readline

col, row = map(int, read().split())


def check(tomatomap):
    for row in tomatomap:
        if 0 in row:
            return False
    return True


def bfs(tomatomap):
    queue = deque()
    for i in range(row):
        for j in range(col):
            if tomatomap[i][j] == 1:
                queue.append((j, i))
    
    day = 0
    while queue:
        x, y = queue.popleft()
        day = tomatomap[y][x]

        for move in [(0, 1), (1, 0), (0, -1), (-1, 0)]: # D,R,U,L
            move_x, move_y = x + move[0], y + move[1]
            if (0 <= move_x < col) and (0 <= move_y < row) and tomatomap[move_y][move_x] == 0:
                queue.append((move_x, move_y))
                tomatomap[move_y][move_x] = day + 1
    
    print(day - 1 if check(tomatomap) else -1)


tomatomap = [list(map(int, read().split())) for _ in range(row)]
bfs(tomatomap)
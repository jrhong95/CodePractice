import sys
from collections import deque

read = sys.stdin.readline

N = int(read())
board = [[0] * N for _ in range(N)]

# input K
for _ in range(int(read())):
    r, c = map(int, read().split())
    board[r - 1][c - 1] = "A"

move = deque()
for _ in range(int(read())):
    n, m = map(str, read().split())
    move.append((int(n), m))

time = 0
snake, dir = deque([(0, 0)]), [0, 1]
while True:
    time += 1
    snake.append((snake[-1][0] + dir[0], snake[-1][1] + dir[1]))

    head_r, head_c = snake.pop()
    # 벽에 부딫힌 경우
    if head_r < 0 or head_r >= N or head_c < 0 or head_c >= N:
        break
    # 뱀에 부딫힌 경우
    elif (head_r, head_c) in snake:
        break
    # 사과인경우
    elif board[head_r][head_c] == "A":
        board[head_r][head_c] = 0
    # 사과가 없는 경우
    else:
        snake.popleft()

    snake.append((head_r, head_c))

    # 방향전환
    if move and time == move[0][0]:
        _, next_dir = move.popleft()
        if next_dir == "D":
            if dir[0] != 0:
                dir = [0, -dir[0]]
            else:
                dir = [dir[1], dir[0]]
        else:
            if dir[0] == 0:
                dir = [-dir[1], 0]
            else:
                dir = [dir[1], dir[0]]

print(time)
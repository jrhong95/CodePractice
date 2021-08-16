import sys
from collections import deque

read = sys.stdin.readline

#    0.상 1.하 2.좌 3.우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

R, C = map(int, read().split())
board = [list(read().rstrip()) for _ in range(R)]

for i in range(R):
    for j in range(C):
        if board[i][j] == "R":
            red_r, red_c = i, j
            board[i][j] = "."
        elif board[i][j] == "B":
            blue_r, blue_c = i, j
            board[i][j] = "."

visited = [[[[False] * C for _ in range(R)] for __ in range(C)] for ___ in range(R)]


def move_ball(direction, r, c):
    is_goal = False
    count = 0

    while True:
        if board[r][c] == "O":  # 목적지에 도착한 경우
            is_goal = True
            break

        if board[r + dr[direction]][c + dc[direction]] == "#":  # 가로막힐 경우
            break

        r += dr[direction]
        c += dc[direction]
        count += 1

    return r, c, count, is_goal


def bfs():
    queue = deque()
    queue.append((red_r, red_c, blue_r, blue_c, 0))

    while queue:
        rr, rc, br, bc, count = queue.popleft()

        if count >= 10:
            break

        for i in range(4):
            r_mr, r_mc, r_count, r_goal = move_ball(i, rr, rc)
            b_mr, b_mc, b_count, b_goal = move_ball(i, br, bc)

            if b_goal:
                continue
            elif r_goal:
                return count + 1

            if r_mr == b_mr and r_mc == b_mc:  # 같은 위치일 경우
                if r_count > b_count:  # 빨간공이 더 많이 움직였을 경우
                    r_mr -= dr[i]
                    r_mc -= dc[i]
                else:  # 파란공이 더 많이 움직였을 경우
                    b_mr -= dr[i]
                    b_mc -= dc[i]

            if visited[r_mr][r_mc][b_mr][b_mc]:  # 둘 다 방문한 적이 있으면
                continue

            visited[r_mr][r_mc][b_mr][b_mc] = True

            queue.append((r_mr, r_mc, b_mr, b_mc, count + 1))

    return -1


print(bfs())
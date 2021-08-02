import sys

read = sys.stdin.readline

R, C, cr, cc, K = map(int, read().split())
board = [list(map(int, read().split())) for _ in range(R)]
commands = list(map(int, read().split()))
dice = [0] * 6
top, bottom = 1, 3
left, right = 4, 5


def move(direction):
    global top, bottom, left, right, cr, cc
    if direction == 1:  # 우
        if cc + 1 >= C:
            return False
        cc += 1
        dice[top], dice[right], dice[bottom], dice[left] = (
            dice[left],
            dice[top],
            dice[right],
            dice[bottom],
        )
    elif direction == 2:  # 좌
        if cc - 1 < 0:
            return False
        cc -= 1
        dice[top], dice[right], dice[bottom], dice[left] = (
            dice[right],
            dice[bottom],
            dice[left],
            dice[top],
        )
    elif direction == 3:  # 상
        if cr - 1 < 0:
            return False
        cr -= 1
        top = top + 1 if top + 1 < 4 else 0
        bottom = bottom + 1 if bottom + 1 < 4 else 0
    elif direction == 4:  # 하
        if cr + 1 >= R:
            return False
        cr += 1
        top = top - 1 if top - 1 >= 0 else 3
        bottom = bottom - 1 if bottom - 1 >= 0 else 3

    return True


for command in commands:
    if move(command):
        if board[cr][cc] == 0:
            board[cr][cc] = dice[bottom]
        else:
            dice[bottom] = board[cr][cc]
            board[cr][cc] = 0
        print(dice[top])
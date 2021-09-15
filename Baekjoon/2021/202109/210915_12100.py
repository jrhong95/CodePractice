import sys

sys.setrecursionlimit(10 ** 6)
from copy import deepcopy

read = sys.stdin.readline

# 0: left, 1: right, 2: up, 3: down
def move(prev_board, dir):
    global answer, N
    board = deepcopy(prev_board)
    if dir == 0:
        for r in range(N):
            tr, tc = r, 0
            for c in range(N):
                if board[r][c] == 0 or (tr == r and tc == c):  # 움직일 번호가 없을 때, 제자리 일 때
                    continue
                if board[tr][tc] == 0:  # 이동할 곳이 비었을 때
                    board[tr][tc], board[r][c] = board[r][c], 0
                elif board[tr][tc] == board[r][c]:  # 이동할 곳과 같은 숫자일 때
                    board[tr][tc] += board[r][c]
                    board[r][c] = 0
                    tc += 1
                else:  # 그 자리에 이동할 수 없을 때
                    tc += 1
                    if not (tr == r and tc == c):
                        board[tr][tc] = board[r][c]
                        board[r][c] = 0
    elif dir == 1:
        for r in range(N):
            tr, tc = r, N - 1
            for c in range(N - 1, -1, -1):
                if board[r][c] == 0 or (tr == r and tc == c):  # 움직일 번호가 없을 때, 제자리 일 때
                    continue
                if board[tr][tc] == 0:  # 이동할 곳이 비었을 때
                    board[tr][tc], board[r][c] = board[r][c], 0
                elif board[tr][tc] == board[r][c]:  # 이동할 곳과 같은 숫자일 때
                    board[tr][tc] += board[r][c]
                    board[r][c] = 0
                    tc -= 1
                else:  # 그 자리에 이동할 수 없을 때
                    tc -= 1
                    if not (tr == r and tc == c):
                        board[tr][tc] = board[r][c]
                        board[r][c] = 0
    elif dir == 2:
        for c in range(N):
            tr, tc = 0, c
            for r in range(N):
                if board[r][c] == 0 or (tr == r and tc == c):  # 움직일 번호가 없을 때, 제자리 일 때
                    continue
                if board[tr][tc] == 0:  # 이동할 곳이 비었을 때
                    board[tr][tc], board[r][c] = board[r][c], 0
                elif board[tr][tc] == board[r][c]:  # 이동할 곳과 같은 숫자일 때
                    board[tr][tc] += board[r][c]
                    board[r][c] = 0
                    tr += 1
                else:  # 그 자리에 이동할 수 없을 때
                    tr += 1
                    if not (tr == r and tc == c):
                        board[tr][tc] = board[r][c]
                        board[r][c] = 0
    else:
        for c in range(N):
            tr, tc = N - 1, c
            for r in range(N - 1, -1, -1):
                if board[r][c] == 0 or (tr == r and tc == c):  # 움직일 번호가 없을 때, 제자리 일 때
                    continue
                if board[tr][tc] == 0:  # 이동할 곳이 비었을 때
                    board[tr][tc], board[r][c] = board[r][c], 0
                elif board[tr][tc] == board[r][c]:  # 이동할 곳과 같은 숫자일 때
                    board[tr][tc] += board[r][c]
                    board[r][c] = 0
                    tr -= 1
                else:  # 그 자리에 이동할 수 없을 때
                    tr -= 1
                    if not (tr == r and tc == c):
                        board[tr][tc] = board[r][c]
                        board[r][c] = 0
    answer = max(max(max(line) for line in board), answer)
    return board


def backtracking(cnt, board):
    if cnt > 5:
        return
    for i in range(4):
        backtracking(cnt + 1, move(board, i))


def main():
    global answer, N
    answer = 0
    N = int(read())
    board = [list(map(int, read().split())) for _ in range(N)]
    backtracking(1, board)
    print(answer)


main()

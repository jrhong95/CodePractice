import sys

read = sys.stdin.readline
dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]
reverse_dir = [1, 0, 3, 2]

N, K = map(int, read().split())
board = [list(map(int, read().split())) for _ in range(N)]
mals = [list(map(lambda x: int(x) - 1, read().split())) for _ in range(K)]
board_mal = [[[] for __ in range(N)] for _ in range(N)]


def main():
    for i, cur in enumerate(mals):
        r, c, _ = cur
        board_mal[r][c].append(i)

    count = 0

    while count <= 1000:
        count += 1
        for i, mal in enumerate(mals):
            if move(mal, i):
                return count
    return -1


def move(mal, mal_num):
    r, c, direction = mal
    if board_mal[r][c][0] != mal_num:  # 맨 아래 번호가 현재 말 번호랑 다를 시
        return False

    nr, nc = r + dr[direction], c + dc[direction]

    if not 0 <= nr < N or not 0 <= nc < N or board[nr][nc] == 2:  # 벗어나거나 파랑일 경우
        direction = reverse_dir[direction]
        mals[mal_num][2] = direction
        nr, nc = r + dr[direction], c + dc[direction]
        if not 0 <= nr < N or not 0 <= nc < N or board[nr][nc] == 2:  # 그래도 벗어나거나 파랑일 경우
            return False

    if board[nr][nc] == 0:  # 이동할 판이 흰색인 경우
        board_mal[nr][nc].extend(board_mal[r][c])  # 모두 엎음
        board_mal[r][c] = []  # 원래 있던 곳 초기화
    else:  # 이동할 판이 빨간색인 경우
        board_mal[r][c].reverse()  # 먼저 뒤집는다.
        board_mal[nr][nc].extend(board_mal[r][c])  # 그리고 엎음
        board_mal[r][c] = []  # 초기화

    for n in board_mal[nr][nc]:
        mals[n][0], mals[n][1] = nr, nc

    if len(board_mal[nr][nc]) >= 4:
        return True

    return False


print(main())
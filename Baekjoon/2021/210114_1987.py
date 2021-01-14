import sys
read = sys.stdin.readline

row, col = map(int, read().split())
board = [list(read().rstrip()) for _ in range(row)]
visited = [False for _ in range(26)]
visited[ord(board[0][0]) % 65] = True
max_val = 0


def dfs(start, count):
    global max_val
    r, c = start

    max_val = max(max_val, count)

    for move in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
        move_r, move_c = r + move[0], c + move[1]
        if 0 <= move_r < row and 0 <= move_c < col and not visited[ord(board[move_r][move_c]) % 65]:
            visited[ord(board[move_r][move_c]) % 65] = True
            dfs((move_r, move_c), count + 1)
            visited[ord(board[move_r][move_c]) % 65] = False


dfs((0, 0), 1)
print(max_val)

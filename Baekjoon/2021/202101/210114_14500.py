import sys
read = sys.stdin.readline


row, col = map(int, read().split())
board = [list(map(int, read().split())) for _ in range(row)]
max_vals = []

for i in range(row):

    for j in range(col):
        if j + 3 < col:
            max_vals.append(board[i][j] + board[i][j + 1] +
                            board[i][j + 2] + board[i][j + 3])

        if i + 3 < row:
            max_vals.append(board[i][j] + board[i + 1][j] +
                            board[i + 2][j] + board[i + 3][j])

        if j + 1 < col and i + 1 < row:
            max_vals.append(board[i][j] + board[i][j + 1] +
                            board[i + 1][j] + board[i + 1][j + 1])

        if j + 2 < col and i + 1 < row:
            max_vals.append(board[i][j + 1] + board[i + 1]
                            [j] + board[i + 1][j + 1] + board[i + 1][j + 2])

        if j + 2 < col and i + 1 < row:
            max_vals.append(board[i + 1][j + 1] + board[i]
                            [j] + board[i][j + 1] + board[i][j + 2])

        if j + 1 < col and i + 2 < row:
            max_vals.append(board[i + 1][j] + board[i]
                            [j + 1] + board[i + 1][j + 1] + board[i + 2][j + 1])

        if j + 1 < col and i + 2 < row:
            max_vals.append(board[i + 1][j + 1] + board[i]
                            [j] + board[i + 1][j] + board[i + 2][j])

        if j + 1 < col and i + 2 < row:
            max_vals.append(board[i][j] + board[i][j + 1] +
                            board[i + 1][j + 1] + board[i + 2][j + 1])

        if j + 1 < col and i + 2 < row:
            max_vals.append(board[i][j] + board[i][j + 1] +
                            board[i + 1][j] + board[i + 2][j])

        if j + 1 < col and i + 2 < row:
            max_vals.append(board[i][j] + board[i + 1][j] +
                            board[i + 2][j] + board[i + 2][j + 1])

        if j + 1 < col and i + 2 < row:
            max_vals.append(board[i + 2][j] + board[i][j + 1] +
                            board[i + 1][j + 1] + board[i + 2][j + 1])

        if j + 2 < col and i + 1 < row:
            max_vals.append(board[i][j] + board[i][j + 1] +
                            board[i][j + 2] + board[i + 1][j])

        if j + 2 < col and i + 1 < row:
            max_vals.append(board[i][j + 2] + board[i + 1][j] +
                            board[i + 1][j + 1] + board[i + 1][j + 2])

        if j + 2 < col and i + 1 < row:
            max_vals.append(board[i][j] + board[i + 1][j] +
                            board[i + 1][j + 1] + board[i + 1][j + 2])

        if j + 2 < col and i + 1 < row:
            max_vals.append(board[i][j] + board[i][j + 1] +
                            board[i][j + 2] + board[i + 1][j + 2])

        if j + 2 < col and i + 1 < row:
            max_vals.append(board[i][j] + board[i][j + 1] +
                            board[i][j + 2] + board[i + 1][j])

        if j + 1 < col and i + 2 < row:
            max_vals.append(board[i][j] + board[i + 1][j] +
                            board[i + 1][j + 1] + board[i + 2][j + 1])

        if j + 1 < col and i + 2 < row:
            max_vals.append(board[i][j + 1] + board[i + 1][j] +
                            board[i + 1][j + 1] + board[i + 2][j])

        if j + 2 < col and i + 1 < row:
            max_vals.append(board[i][j] + board[i][j + 1] +
                            board[i + 1][j + 1] + board[i + 1][j + 2])

        if j + 2 < col and i + 1 < row:
            max_vals.append(board[i][j + 1] + board[i][j + 2] +
                            board[i + 1][j] + board[i + 1][j + 1])

print(max(max_vals))

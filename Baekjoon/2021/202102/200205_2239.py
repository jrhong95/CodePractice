import sys
read = sys.stdin.readline

sudoku = [list(map(int, list(read().rstrip()))) for _ in range(9)]


def check(r, c):
    check = [True] * 9
    check_r, check_c = (r // 3) * 3, (c // 3) * 3

    for i in range(9):
        if sudoku[r][i] != 0:
            check[sudoku[r][i] - 1] = False
        if sudoku[i][c] != 0:
            check[sudoku[i][c] - 1] = False

    for i in range(check_r, check_r + 3):
        for j in range(check_c, check_c + 3):
            if sudoku[i][j] != 0:
                check[sudoku[i][j] - 1] = False

    return [i + 1 for i, n in enumerate(check) if n]


def solve(n):
    global fin

    if n == len(empty):
        fin = True
        return

    r, c = empty[n]
    for num in check(r, c):
        sudoku[r][c] = num
        solve(n + 1)
        if fin:
            return
        sudoku[r][c] = 0


fin = False
empty = []
for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            empty.append((i, j))
solve(0)

for line in sudoku:
    print(''.join(str(n) for n in line))

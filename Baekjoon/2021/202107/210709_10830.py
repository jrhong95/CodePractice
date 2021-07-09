import sys

read = sys.stdin.readline


def mul_matrix(matrix1, matrix2, N):
    new_matrix = []
    for i in range(N):
        row = [sum(matrix1[i][k] * matrix2[k][j] for k in range(N)) % 1000 for j in range(N)]
        new_matrix.append(row)

    return new_matrix


def div_conq(matrix, N, sq):
    if sq == 1:
        return matrix
    elif sq % 2:  # 홀수
        return mul_matrix(div_conq(matrix, N, sq - 1), matrix, N)
    else:
        cur_matrix = div_conq(matrix, N, sq // 2)
        return mul_matrix(cur_matrix, cur_matrix, N)


def solution():
    N, B = map(int, read().split())
    matrix = [list(map(lambda x: int(x) % 1000, read().split())) for _ in range(N)]
    for row in div_conq(matrix, N, B):
        print(*row, sep=" ")


solution()
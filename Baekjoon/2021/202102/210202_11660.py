import pprint
import sys
read = sys.stdin.readline

N, TC = map(int, read().split())
matrix = [[0] * (N + 1)] + [[0] + list(map(int, read().split()))
                            for _ in range(N)]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if j != 1:
            matrix[i][j] = matrix[i][j] + matrix[i][j - 1] + \
                matrix[i - 1][j] - matrix[i - 1][j - 1]
        else:
            matrix[i][j] += matrix[i - 1][j]

for _ in range(TC):
    r1, c1, r2, c2 = map(int, read().split())
    print(matrix[r2][c2] - matrix[r2][c1 - 1] -
          matrix[r1 - 1][c2] + matrix[r1 - 1][c1 - 1])

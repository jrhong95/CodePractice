import sys
read = sys.stdin.readline

N, M = map(int, read().split())
matrix = [list(map(int, list(read().rstrip()))) for _ in range(N)]
max_size = 1

for i in range(N - 1):
    for j in range(M - 1):
        si, sj = i + 1, j + 1
        while si < N and sj < M:
            if matrix[i][j] == matrix[si][sj] == matrix[si][j] == matrix[i][sj]:
                max_size = max(max_size, (si - i + 1) ** 2)
            si += 1
            sj += 1

print(max_size)

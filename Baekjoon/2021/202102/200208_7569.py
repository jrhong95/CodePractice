import sys
from collections import deque
read = sys.stdin.readline


def check(h, r, c, num):
    return True if matrix[h][r][c] == num else False


def bfs(tomatos):
    queue = deque()
    queue.extend(map(lambda x: (x, 0), tomatos))
    days = 0
    while queue:
        idx, days = queue.popleft()
        h, i, j = idx
        for nh, ni, nj in moves:
            mh, mi, mj = nh + h, ni + i, nj + j
            if 0 <= mh < H and 0 <= mi < N and 0 <= mj < M and check(mh, mi, mj, 0):
                matrix[mh][mi][mj] = 1
                queue.append(((mh, mi, mj), days + 1))

    return days


def solve():
    tmp = []
    for h in range(H):
        for i in range(N):
            tmp.extend([(h, i, j) for j in range(M) if check(h, i, j, 1)])

    ans = bfs(tmp)

    for h in range(H):
        for i in range(N):
            for j in range(M):
                if check(h, i, j, 0):
                    print(-1)
                    return
    print(ans)


M, N, H = map(int, read().split())
moves = [(1, 0, 0), (-1, 0, 0), (0, 0, -1), (0, 0, 1), (0, 1, 0), (0, -1, 0)]
matrix = []

for _ in range(H):
    matrix.append([list(map(int, read().split())) for _ in range(N)])

solve()

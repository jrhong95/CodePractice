import sys
from copy import deepcopy
from collections import deque

read = sys.stdin.readline

WALL_CNT = 3
mr = [0, -1, 0, 1]
mc = [1, 0, -1, 0]


R, C = map(int, read().split())
lab = [list(map(int, read().split())) for _ in range(R)]
max_area = 0


# BFS
def spread_virus(virus_lab):
    queue = deque()
    visited = [[False] * C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if virus_lab[r][c] == 2:
                queue.append((r, c))
                visited[r][c] = True

    while queue:
        r, c = queue.popleft()
        for tr, tc in zip(mr, mc):
            nr = r + tr
            nc = c + tc

            if 0 <= nr < R and 0 <= nc < C and virus_lab[nr][nc] == 0:
                if not visited[nr][nc]:
                    virus_lab[nr][nc] = 2
                    queue.append((nr, nc))

    return virus_lab


def count_safe_area(virus_lab):
    s = sum(line.count(0) for line in virus_lab)
    return s


def make_wall(r, c, count):
    global max_area

    if count == WALL_CNT:
        max_area = max(max_area, count_safe_area(spread_virus(deepcopy(lab))))
    else:
        for i in range(r, R):
            for j in range(c, C):
                if lab[i][j] == 0:
                    lab[i][j] = 1
                    make_wall(i, j, count + 1)
                    lab[i][j] = 0
            c = 0  # 해당 열에서 내려가면 0으로 초기화


def main():
    make_wall(0, 0, 0)
    print(max_area)


main()
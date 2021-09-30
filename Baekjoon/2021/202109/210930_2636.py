import sys
from collections import deque

read = sys.stdin.readline

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def main():
    global R, C, cheeze, visited
    R, C = map(int, read().split())
    cheeze = [list(map(int, read().split())) for _ in range(R)]
    visited = [[False] * C for _ in range(R)]
    cheeze_count = sum(line.count(1) for line in cheeze)
    answer = 0
    air = [(0, 0)]

    while True:
        melted_cheeze = set()
        while air:
            r, c = air.pop()
            melted_cheeze.update(find_melt_cheeze(r, c))

        if cheeze_count - len(melted_cheeze) == 0:
            return answer, cheeze_count
        answer += 1
        cheeze_count -= len(melted_cheeze)
        for r, c in melted_cheeze:
            cheeze[r][c] = 0
            air.append((r, c))


def find_melt_cheeze(i, j):
    global R, C, cheeze, visited
    queue = deque()

    if visited[i][j]:
        return []
    queue.append((i, j))
    visited[i][j] = True

    cheeze_queue = []
    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if not 0 <= nr < R or not 0 <= nc < C or visited[nr][nc]:
                continue
            if cheeze[nr][nc] == 1:  # 치즈일 경우
                cheeze_queue.append((nr, nc))
            else:
                queue.append((nr, nc))
                visited[nr][nc] = True

    return cheeze_queue


day, count = main()
print(day + 1)
print(count)
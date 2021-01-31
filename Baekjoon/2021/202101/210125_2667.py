import sys
from collections import deque
read = sys.stdin.readline


def bfs(r, c, town):
    queue = deque([(r, c)])
    town[r][c] = 0
    count = 0

    while queue:
        r, c = queue.popleft()
        count += 1

        for move in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            move_r, move_c = r + move[0], c + move[1]

            if 0 <= move_r < N and 0 <= move_c < N and town[move_r][move_c] == 1:
                queue.append((move_r, move_c))
                town[move_r][move_c] = 0

    return count


N = int(read())
town = [list(map(int, list(read().rstrip()))) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

answer = []
for i in range(N):
    for j in range(N):
        if town[i][j] == 1:
            answer.append(bfs(i, j, town))

print(len(answer))
print(*sorted(answer), sep='\n')

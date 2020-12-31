from collections import deque


def dfs(start, field):
    q = deque()
    q.append(start)

    while q:
        x, y = q.popleft()
        field[y][x] = 0

        for move in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            mx, my = move[0] + x, move[1] + y
            if mx < M and mx >= 0 and my < N and my >= 0 and field[my][mx] == 1:
                if (mx, my) not in q:
                    q.append((mx, my))


for _ in range(int(input())):
    M, N, K = map(int, input().split())
    field = [[0] * M for _ in range(N)]
    cnt = 0

    for _ in range(K):
        x, y = map(int, input().split())
        field[y][x] = 1

    for h in range(N):
        for w in range(M):
            if field[h][w] == 1:
                dfs((w, h), field)
                cnt += 1

    print(cnt)

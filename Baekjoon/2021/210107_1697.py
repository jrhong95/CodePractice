from collections import deque


def bfs(start):
    queue = deque()

    visit = [False for _ in range(100001)]
    queue.append((start, 0))
    visit[start] = True

    while queue:
        point = queue.popleft()

        if point[0] == K:
            return point[1]

        for i in [point[0] + 1, point[0] - 1, point[0] * 2]:
            if (0 <= i < 100001) and not visit[i]:
                queue.append((i, point[1] + 1))
                visit[i] = True


N, K = map(int, input().split())

if N >= K:
    print(N - K)
else:
    print(bfs(N))

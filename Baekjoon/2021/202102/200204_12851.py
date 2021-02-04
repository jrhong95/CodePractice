from collections import deque


def bfs(start):
    queue = deque()

    visit = [[float('inf'), 0] for _ in range(100001)]  # 시간, 여기까지 오는 방법 수
    queue.append((start, 0, False))
    visit[start] = [0, 1]

    while queue:
        time, way_count, break_flag = queue.popleft()

        if break_flag:
            break

        for i in [time + 1, time - 1, time * 2]:
            if (0 <= i < 100001) and way_count + 1 <= visit[i][0]:
                visit[i][0] = way_count + 1
                visit[i][1] += 1

                break_flag = True if i == K else False
                queue.append((i, way_count + 1, break_flag))

    return visit[K][0:2]


N, K = map(int, input().split())

if N >= K:
    print(N - K)
    print(1)
else:
    print(*bfs(N), sep='\n')

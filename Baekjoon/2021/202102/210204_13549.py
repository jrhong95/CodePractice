from heapq import heappop, heappush


def bfs(start):
    heap = [(0, start)]

    visit = [False for _ in range(100001)]
    visit[start] = True

    while heap:
        time, pos = heappop(heap)

        if pos == K:
            return time

        for idx, i in enumerate([pos * 2, pos + 1, pos - 1]):
            if (0 <= i < 100001) and not visit[i]:
                if idx == 0:
                    heappush(heap, (time, i))
                else:
                    heappush(heap, (time + 1, i))

                visit[i] = True


N, K = map(int, input().split())

print(bfs(N))

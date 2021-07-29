import sys
from heapq import *

INF = sys.maxsize
read = sys.stdin.readline

N, M, K = map(int, read().split())
graph = [[] for _ in range(N + 1)]
dist = [[] for _ in range(N + 1)]


def main():
    for _ in range(M):
        a, b, c = map(int, read().split())
        graph[a].append((b, c))

    dijstra()

    for i in range(1, N + 1):
        print(-heappop(dist[i]) if len(dist[i]) == K else -1)


def dijstra():
    heap = []
    heappush(heap, (0, 1))  # cost, node
    heappush(dist[1], 0)

    while heap:
        cur_cost, cur_node = heappop(heap)

        for next_node, next_cost in graph[cur_node]:
            # K개 만큼 없는 경우
            if len(dist[next_node]) < K:
                # 그냥 넣는다, 최대힙이기 때문에 음수로 바꿔서 넣음
                heappush(dist[next_node], -(cur_cost + next_cost))
                # 다익스트라 heap에 다음 간선에 대한 정보 넣음.
                heappush(heap, (cur_cost + next_cost, next_node))

            # K개 이상 있고 가장 느린 경로보다 빠른 경로가 있는 경우
            elif -dist[next_node][0] > cur_cost + next_cost:
                # 가중치의 개수를 K개로 맞춰주기 위해 뺐다가 새로운 가중치 넣음
                heappop(dist[next_node])
                heappush(dist[next_node], -(cur_cost + next_cost))
                # 다익스트라 heap에 다음 간선에 대한 정보 넣음.
                heappush(heap, (cur_cost + next_cost, next_node))


main()

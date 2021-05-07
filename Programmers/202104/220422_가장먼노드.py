from collections import defaultdict, Counter
import heapq as hq

START = 1
INF = 10 ** 9


def solution(n, edge):
    matrix = defaultdict(list)

    for v1, v2 in edge:
        matrix[v1].append(v2)
        matrix[v2].append(v1)

    distance = [INF] * (n + 1)
    distance[START] = 0

    heap = []
    hq.heappush(heap, (0, START))

    while heap:
        dist, node = hq.heappop(heap)

        if dist > distance[node]:
            continue

        for next_node in matrix[node]:
            next_dist = 1 + dist

            if next_dist < distance[next_node]:
                hq.heappush(heap, (next_dist, next_node))
                distance[next_node] = next_dist

    ans = Counter(distance[1:])

    return ans[max(list(ans))]
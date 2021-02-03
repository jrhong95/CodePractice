import pprint
import sys
read = sys.stdin.readline
INF = sys.maxsize


def floyd_warshall():
    min_distance = [[0] * N for _ in range(N)]

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            min_distance[i - 1][j - 1] = 0 if i == j else graph[i][j]

    for k in range(N):
        for i in range(N):
            for j in range(N):
                min_distance[i][j] = min(
                    min_distance[i][k] + min_distance[k][j], min_distance[i][j])

    for line in min_distance:
        for n in line:
            print(0 if n >= INF else n, end=' ')
        print()


N = int(read())
graph = [[INF] * (N + 1) for _ in range(N + 1)]

for _ in range(int(read())):
    a, b, c = map(int, read().split())
    if graph[a][b] > c:
        graph[a][b] = c

floyd_warshall()

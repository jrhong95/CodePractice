import pprint


def solution(n, s, a, b, fares):
    INF = 10 ** 9
    answer = INF
    distance = [[INF] * (n + 1) for _ in range(n + 1)]

    for v1, v2, d in fares:
        distance[v1][v2] = min(distance[v1][v2], d)
        distance[v2][v1] = min(distance[v2][v1], d)

    for i in range(1, n + 1):
        distance[i][i] = 0

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

    for wp in range(1, n + 1):
        answer = min(answer, distance[s][wp] + distance[wp][a] + distance[wp][b])
    return answer


print(
    solution(
        6,
        4,
        6,
        2,
        [
            [4, 1, 10],
            [3, 5, 24],
            [5, 6, 2],
            [3, 1, 41],
            [5, 1, 24],
            [4, 6, 50],
            [2, 4, 66],
            [2, 3, 22],
            [1, 6, 25],
        ],
    )
)

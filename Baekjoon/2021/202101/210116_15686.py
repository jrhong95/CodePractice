import sys
from itertools import combinations
read = sys.stdin.readline


def distance(n1, n2):
    return abs(n1[0] - n2[0]) + abs(n1[1] - n2[1])


N, M = map(int, read().split())
town = [list(map(int, read().split())) for _ in range(N)]
houses, chickens = [], []

for i in range(N):
    for j in range(N):
        if town[i][j] == 1:
            houses.append((i, j))
        elif town[i][j] == 2:
            chickens.append((i, j))

ans = 250000
for chicken in combinations(chickens, M):
    chicken_distance = sum(min(distance(house, c)
                               for c in chicken) for house in houses)
    ans = min(ans, chicken_distance)

print(ans)

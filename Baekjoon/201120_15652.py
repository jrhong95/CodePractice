from itertools import combinations_with_replacement


N, M = map(int, input().split())
for i in combinations_with_replacement(range(1, N + 1), M):
    print(*i)  



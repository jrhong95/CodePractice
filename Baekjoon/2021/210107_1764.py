import sys
read = sys.stdin.readline

N, M = map(int, read().split())

d = set(read().rstrip() for _ in range(N))
b = set(read().rstrip() for _ in range(M))
db = sorted(d.intersection(b))

print(len(db))
print(*db, sep='\n')

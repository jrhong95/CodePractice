import sys
from collections import defaultdict

read = sys.stdin.readline

N = int(read())
dict = defaultdict(int)
for n in list(map(int, read().split())):
    dict[n] += 1

M = int(read())
search = list(map(int, read().split()))

for s in search:
    print(dict[s], end=' ')
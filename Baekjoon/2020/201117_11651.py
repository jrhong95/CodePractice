import sys


l = sorted([list(map(int, sys.stdin.readline().split())) for _ in range(int(sys.stdin.readline()))],
        key=lambda x: (x[1], x[0]))
for n in l:
    print(n[0], n[1])
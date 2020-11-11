import sys
for n in sorted([tuple(map(int, sys.stdin.readline().split(" "))) for _ in range(int(sys.stdin.readline()))]):
    print(f"{n[0]} {n[1]}")
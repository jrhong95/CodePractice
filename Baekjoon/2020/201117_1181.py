import sys


l = sorted(list(set([sys.stdin.readline().rstrip() for _ in range(int(sys.stdin.readline()))])),
            key=lambda x: (len(x), x))
for c in l:
    print(c)
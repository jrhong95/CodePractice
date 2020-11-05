import sys


l = [int(sys.stdin.readline()) for _ in range(int(sys.stdin.readline()))]
for n in sorted(l):
    print(n)
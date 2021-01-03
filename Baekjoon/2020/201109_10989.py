import sys


c = [0] * 10001
for i in range(int(sys.stdin.readline())):
    c[int(sys.stdin.readline())] += 1

for idx, n in enumerate(c):
    print(f"{idx}\n" * n, end = '')

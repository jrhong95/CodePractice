import sys

read = sys.stdin.readline

a, b = read().rstrip().split()
diff = len(b) - len(a)

ans = 50
for start in range(diff + 1):
    ans = min(sum(a[i - start] != b[i] for i in range(start, start + len(a))), ans)

print(ans)

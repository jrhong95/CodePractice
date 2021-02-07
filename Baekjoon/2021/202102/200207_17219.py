import sys
read = sys.stdin.readline

N, TC = map(int, read().split())
memo = {}
for _ in range(N):
    site, pwd = read().rstrip().split()
    memo[site] = pwd

for _ in range(TC):
    print(memo[read().rstrip()])

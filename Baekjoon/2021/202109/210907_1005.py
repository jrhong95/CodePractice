import sys
from collections import deque

read = sys.stdin.readline
ans = []
for _ in range(int(read())):
    N, K = map(int, read().split())
    build_time = [-1] + list(map(int, read().split()))

    indegree, dp = [-1] + [0] * N, [0] * (N + 1)
    adjust = [[] for _ in range(N + 1)]
    for __ in range(K):
        a, b = map(int, read().split())
        indegree[b] += 1
        adjust[a].append(b)

    queue = deque()
    for i in range(1, N + 1):
        if indegree[i] == 0:
            queue.append(i)
            dp[i] = build_time[i]

    while queue:
        cur = queue.popleft()
        for n in adjust[cur]:
            indegree[n] -= 1
            dp[n] = max(dp[cur] + build_time[n], dp[n])
            if indegree[n] == 0:
                queue.append(n)

    ans.append(dp[int(read())])

print(*ans, sep="\n")

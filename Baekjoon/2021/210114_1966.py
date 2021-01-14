import sys
from collections import deque
read = sys.stdin.readline


for _ in range(int(read())):
    q = deque()
    N, M = map(int, read().split())

    priority = list(map(int, read().split()))
    q.extend(list(map(lambda x: [x, False], priority)))
    priority = sorted(priority, reverse=True)
    q[M][1] = True

    count = 0
    while True:
        if priority[0] != q[0][0]:
            q.append(q.popleft())
        else:
            node = q.popleft()
            priority.remove(node[0])
            count += 1

            if node[1]:
                break

    print(count)

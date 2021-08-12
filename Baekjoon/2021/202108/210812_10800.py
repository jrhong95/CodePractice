import sys

read = sys.stdin.readline

N = int(read())
colors = [0] * (N + 1)
ans = [0] * (N + 1)
balls = []
for i in range(N):
    color, ball_size = map(int, read().split())
    balls.append((i, color, ball_size))

balls.sort(key=lambda x: x[-1])

j, cumul = 0, 0
for i, ball in enumerate(balls):
    idx, color, size = ball
    while balls[j][2] < size:
        cumul += balls[j][2]
        colors[balls[j][1]] += balls[j][2]
        j += 1

    ans[idx] = cumul - colors[color]

print(*ans[:-1], sep="\n")
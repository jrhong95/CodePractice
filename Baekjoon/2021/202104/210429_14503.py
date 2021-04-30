import sys

read = sys.stdin.readline
dc = (0, -1, 0, 1)
dr = (-1, 0, 1, 0)
# N, W, S, E


def is_cleanable(pos):
    r, c, d = pos

    r += dr[d]
    c += dc[d]

    return True if room[r][c] == 0 else False


N, M = map(int, read().split())
r, c, d = map(int, read().split())

if d == 1:
    d = 3
elif d == 3:
    d = 1

pos = (r, c, d)
room = [list(map(int, read().split())) for _ in range(N)]
clean = 0

while True:
    r, c, d = pos
    if room[r][c] == 0:
        clean += 1
        room[r][c] = 2

    rotate_count = 0
    while rotate_count < 4:
        d = d + 1 if d < 3 else 0
        pos = (r, c, d)
        if not is_cleanable(pos):  # 청소 할 수 없으면
            rotate_count += 1
        else:
            r, c, d = pos
            r += dr[d]
            c += dc[d]
            pos = (r, c, d)
            break  # 청소할 수 있는 경우

    if rotate_count == 4:  #   후진
        r, c, d = pos
        r -= dr[d]
        c -= dc[d]
        pos = (r, c, d)
        if room[r][c] == 1:
            break

print(clean)

import sys
from collections import deque

read = sys.stdin.readline

mr = [-2, -1, 1, 2, 2, 1, -1, -2]
mc = [1, 2, 2, 1, -1, -2, -2, -1]


def main():
    for _ in range(int(read())):
        size = int(read())
        start = tuple(map(int, read().split()))
        end = tuple(map(int, read().split()))

        print(bfs(start, end, size))


def bfs(start, end, size):
    board = [[False] * size for _ in range(size)]
    queue = deque([(start[0], start[1], 0)])  # pos, count
    board[start[0]][start[1]] = True

    while queue:
        r, c, count = queue.popleft()

        if r == end[0] and c == end[1]:
            return count

        for tr, tc in zip(mr, mc):
            cr = tr + r
            cc = tc + c

            if 0 <= cr < size and 0 <= cc < size and not board[cr][cc]:
                board[cr][cc] = True
                queue.append((cr, cc, count + 1))


main()
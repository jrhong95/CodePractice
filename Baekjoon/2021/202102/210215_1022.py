import sys
import pprint
read = sys.stdin.readline
move = [(0, 1), (-1, 0), (0, -1), (1, 0)]

r1, c1, r2, c2 = map(int, read().split())
size = max(list(map(abs, [r1, c1, r2, c2])))

matrix = [[0] * (size * 2 + 1) for _ in range((size * 2 + 1))]

jump, jump_count, idx, count = 1, 0, -1, 1
r, c = size, size

for i in range(1, ((size * 2 + 1) ** 2 + 1)):
    matrix[r][c] = i

    if count == jump:
        idx = 0 if idx == 3 else idx + 1

        if jump_count == 2:
            jump_count = 1
            jump += 1
        else:
            jump_count += 1
        count = 1

    else:
        count += 1

    r += move[idx][0]
    c += move[idx][1]

blnk_size = len(str((size * 2 + 1) ** 2))
print(blnk_size)
for i in range(r2 - r1 + 1):
    for j in range(c2 - c1 + 1):
        print(f"{matrix[i][j]: >{blnk_size}}", end=' ')
    print()

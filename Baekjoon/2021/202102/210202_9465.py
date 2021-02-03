import sys
read = sys.stdin.readline

for _ in range(int(read())):
    N = int(read())
    sticker = [[0, 0] + list(map(int, read().split())) for _ in range(2)]

    for i in range(2, N + 2):
        sticker[0][i] = max(sticker[1][i - 1], sticker[1]
                            [i - 2]) + sticker[0][i]
        sticker[1][i] = max(sticker[0][i - 1], sticker[0]
                            [i - 2]) + sticker[1][i]

    print(max(sticker[0][N + 1], sticker[1][N + 1]))

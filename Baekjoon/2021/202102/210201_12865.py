import sys
read = sys.stdin.readline


def solve():
    N, max_weight = map(int, read().split())
    dp = {0: 0}

    for _ in range(N):
        w, v = map(int, read().split())
        tmp = {}
        for prev_w, prev_v in dp.items():
            if prev_w + w <= max_weight and dp.get(prev_w + w, 0) < prev_v + v:
                tmp[prev_w + w] = prev_v + v
        dp.update(tmp)

    print(max(dp.values()))


def solve1():
    N, max_weight = map(int, read().split())
    dp = [[0] * (max_weight + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        w, v = map(int, read().split())

        for bag_size in range(1, max_weight + 1):
            if w > bag_size:
                dp[i][bag_size] = dp[i - 1][bag_size]
            else:
                dp[i][bag_size] = max(dp[i - 1][bag_size],
                                      dp[i - 1][bag_size - w] + v)

    print(dp[N][max_weight])


solve()

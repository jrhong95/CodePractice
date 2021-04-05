import sys
read = sys.stdin.readline

N, K = map(int, read().split())
coins = [int(read()) for _ in range(N)][::-1]

ans = 0
for coin in coins:
    if coin <= K:
        ans += K // coin
        K %= coin

    if K == 0:
        break

print(ans)

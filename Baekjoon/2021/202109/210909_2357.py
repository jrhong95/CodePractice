import sys

INF = sys.maxsize
read = sys.stdin.readline

N, M = map(int, read().split())
nums = [int(read()) for _ in range(N)]
queries = [tuple(map(lambda x: int(x) - 1, read().split())) for _ in range(M)]

S = 1
while S < N:
    S *= 2

min_tree = [INF] * (S * 2)
max_tree = [INF] * (S * 2)
for i in range(N):
    min_tree[S + i] = nums[i]
    max_tree[S + i] = nums[i]


def init_tree():
    for i in range(S - 1, 0, -1):
        min_tree[i] = min(min_tree[i * 2], min_tree[i * 2 + 1])
        max_tree[i] = max(max_tree[i * 2], max_tree[i * 2 + 1])


def find_min(left, right):
    left += S
    right += S
    ret = INF
    while left <= right:
        if left % 2 == 1:
            ret = min(ret, min_tree[left])
            left += 1
        if right % 2 == 0:
            ret = min(ret, min_tree[right])
            right -= 1

        left //= 2
        right //= 2

    return ret


def find_max(left, right):
    left += S
    right += S
    ret = 0
    while left <= right:
        if left % 2 == 1:
            ret = max(ret, max_tree[left])
            left += 1
        if right % 2 == 0:
            ret = max(ret, max_tree[right])
            right -= 1

        left //= 2
        right //= 2

    return ret


def main():
    init_tree()
    for s, e in queries:
        print(find_min(s, e), end=" ")
        print(find_max(s, e))


main()

import sys

INF = sys.maxsize
read = sys.stdin.readline

N, M = map(int, read().split())
nums = [int(read()) for _ in range(N)]
queries = [tuple(map(lambda x: int(x) - 1, read().split())) for _ in range(M)]

S = 1
while S < N:
    S *= 2

tree = [INF] * (S * 2)
for i in range(N):
    tree[S + i] = nums[i]


def init_tree():
    for i in range(S - 1, 0, -1):
        tree[i] = min(tree[i * 2], tree[i * 2 + 1])


def find(left, right):
    left += S
    right += S
    ret = INF
    while left <= right:
        if left % 2 == 1:
            ret = min(ret, tree[left])
            left += 1
        if right % 2 == 0:
            ret = min(ret, tree[right])
            right -= 1

        left //= 2
        right //= 2

    return ret


def main():
    init_tree()
    for s, e in queries:
        print(find(s, e))


main()

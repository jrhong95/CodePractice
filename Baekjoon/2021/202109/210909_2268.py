import sys

INF = sys.maxsize
read = sys.stdin.readline

N, M = map(int, read().split())
queries = [tuple(map(int, read().split())) for _ in range(M)]

S = 1
while S < N:
    S *= 2
tree = [0] * (S * 2)


def query_sum(left, right):
    left += S
    right += S
    ret = 0
    while left <= right:
        if left % 2 == 1:
            ret = ret + tree[left]
            left += 1
        if right % 2 == 0:
            ret = ret + tree[right]
            right -= 1
        left //= 2
        right //= 2

    return ret


def modify(target, num):
    node = target + S
    tree[node] = num

    node //= 2
    while node > 0:
        tree[node] = tree[node * 2] + tree[node * 2 + 1]
        node //= 2


def main():
    for command, s, e in queries:
        if command == 0:
            if s > e:
                s, e = e, s
            print(query_sum(s - 1, e - 1))
        else:
            modify(s - 1, e)


main()

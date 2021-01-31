import sys
read = sys.stdin.readline


N, M = map(int, read().split())
trees = list(map(int, read().split()))
start, end = 1, max(trees)
answer = 0

while start <= end:
    mid = (start+end) // 2

    extra_tree = 0
    for tree in trees:
        if tree >= mid:
            extra_tree += tree - mid

        if extra_tree >= M:
            start = mid + 1
            answer = mid
            continue

    if extra_tree < M:
        end = mid - 1

print(answer)

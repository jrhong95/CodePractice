import sys

read = sys.stdin.readline


def bi_search(array, target):
    start, end, mid = 0, len(array) - 1, (len(array) - 1) // 2

    while start <= end:
        if array[mid] == target:
            return True
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
        mid = (end + start) // 2

    return False


_ = read()
N = sorted(list(map(int, read().rstrip().split())))
_ = int(read())
M = list(map(int, read().rstrip().split()))
ans = [1 if bi_search(N, item) else 0 for item in M]
print(*ans, sep=" ")

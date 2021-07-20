import math

X, Y = 0, 0


def calc(num):
    return ((Y + num) * 100) // (X + num)


def binary_search(Z):
    start, end, ans = 0, X, -1

    while start <= end:
        mid = (start + end) // 2
        new_Z = calc(mid)

        if new_Z > Z + 1:
            end = mid - 1
        elif new_Z == Z + 1:
            end = mid - 1
            ans = mid
        else:
            start = mid + 1

    return ans if ans > 0 else -1


def solution():
    global X, Y
    X, Y = map(int, input().split())
    Z = calc(0)
    if Z > 98:
        print(-1)
    else:
        print(binary_search(Z))


solution()
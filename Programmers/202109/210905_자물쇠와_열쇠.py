def rotate(key):
    return [[key[j][M - 1 - i] for j in range(M)] for i in range(M)]


def extend_lock(lock):
    size = N + 2 * (M - 1)
    ex_lock = [[0] * size for _ in range(size)]
    for i in range(N):
        for j in range(N):
            ex_lock[i + M - 1][j + M - 1] = lock[i][j]
    return ex_lock


def check(start_r, start_c, key, lock):
    ex_lock = extend_lock(lock)
    for r in range(M):
        for c in range(M):
            ex_lock[start_r + r][start_c + c] += key[r][c]

    for r in range(M - 1, M - 1 + N):
        for c in range(M - 1, M - 1 + N):
            if ex_lock[r][c] != 1:
                return False
    return True


def solution(key, lock):
    global M, N
    M, N = len(key), len(lock)

    for _ in range(4):
        for i in range(N + M - 1):
            for j in range(N + M - 1):
                if check(i, j, key, lock):
                    return True
        key = rotate(key)
    return False
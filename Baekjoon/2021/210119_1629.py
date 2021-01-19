import sys
read = sys.stdin.readline


def solution(A, B, C):
    if B == 0:
        return 1
    elif B == 1:
        return A
    elif B % 2 == 1:
        return solution(A, B - 1, C) * A

    m = solution(A, B // 2, C)
    m %= C
    return (m ** 2) % C


A, B, C = map(int, read().split())
print(solution(A, B, C) % C)

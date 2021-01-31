import sys
from math import gcd
read = sys.stdin.readline


def solve():
    M, N, x, y = map(int, read().split())

    while x <= M * N:
        if x % N == y % N:
            return x
        x += M
    return -1


for _ in range(int(read())):
    print(solve())

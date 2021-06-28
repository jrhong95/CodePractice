from math import gcd
from collections import deque


def solution(arr):
    l = deque(arr)
    while len(l) > 1:
        n1, n2 = l.popleft(), l.popleft()
        l.appendleft(n1 * n2 // gcd(n1, n2))

    return l[0]
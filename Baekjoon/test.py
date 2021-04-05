from itertools import combinations
import sys
raw_input = sys.stdin.readline


n = int(raw_input())
chu = set([1, 3, 7, 26, 94, 259])
for i in range(1, 6):
    for s in set(combinations(chu, i)):
        left = s
        right = chu - set(s)
        l = sum(left) + n
        r = sum(right)
        if sum(left) + n == sum(right):
            print(left)
            print(right)

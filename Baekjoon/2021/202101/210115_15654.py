import sys
from itertools import permutations
read = sys.stdin.readline

N, M = map(int, read().split())
nums = sorted(list(permutations(list(map(int, read().split())), M)))
for num in nums:
    print(" ".join(map(str, num)))

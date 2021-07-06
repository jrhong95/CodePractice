import sys
from itertools import combinations

read = sys.stdin.readline

L, C = map(int, read().split())
nums = sorted(read().rstrip().split())

vowels = "aeiou"

for num in combinations(nums, L):
    v_count, c_count = 0, 0

    for n in num:
        if n in vowels:
            v_count += 1
        else:
            c_count += 1

    if v_count > 0 and c_count > 1:
        print("".join(num))

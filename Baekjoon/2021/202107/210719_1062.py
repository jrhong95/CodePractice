import sys
import string

from itertools import combinations

read = sys.stdin.readline

N, K = map(int, read().split())
char_set = set()
words = [0] * N

for i in range(N):
    word = read().rstrip()[4:-4]
    for c in word:
        words[i] |= 1 << (ord(c) - ord("a"))

if K < 5:
    print(0)
elif K >= 26:
    print(N)
else:
    answer = 0
    antic = {"a", "n", "t", "i", "c"}
    antic_bitmask = 0
    for i in antic:
        antic_bitmask |= 1 << (ord(i) - ord("a"))

    for candidate in combinations(set(list(string.ascii_lowercase)) - antic, K - 5):
        cand_bitmask = antic_bitmask
        for c in candidate:
            cand_bitmask |= 1 << (ord(c) - ord("a"))

        cur_max = 0
        for word in words:
            if cand_bitmask & word == word:
                cur_max += 1
        answer = max(answer, cur_max)

    print(answer)

import sys
from collections import defaultdict
read = sys.stdin.readline

board = defaultdict(int)
R, C, inventory = map(int, read().split())

for _ in range(R):
    for n in list(map(int, read().split())):
        board[n] += 1

min_time, height = sys.maxsize, 0
sorted_key = sorted(board.keys())
for occation in range(sorted_key[0], sorted_key[-1] + 1):
    time = 0
    tmp_inventory = inventory

    for item in board.items():
        if item[0] != occation:
            if item[0] > occation:
                time += 2 * item[1] * (item[0] - occation)
                tmp_inventory += item[1] * (item[0] - occation)
            else:
                time += item[1] * (occation - item[0])
                tmp_inventory -= item[1] * (occation - item[0])

    if tmp_inventory >= 0:
        if min_time >= time:
            min_time = time
            height = occation

print(min_time, height)

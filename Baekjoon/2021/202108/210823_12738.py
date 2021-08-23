import sys
from bisect import bisect_left

read = sys.stdin.readline

N = int(read())
nums = list(map(int, read().split()))
tmp_list = []
max_count = 0

for i, num in enumerate(nums):
    if not tmp_list or tmp_list[-1] < num:
        tmp_list.append(num)
        max_count += 1
    else:
        tmp_list[bisect_left(tmp_list, num)] = num

print(max_count)

import sys
from itertools import permutations

read = sys.stdin.readline

operations = ["+", "-", "*", "/"]
N = int(read())
nums = read().rstrip().split()

ops = []
for i, op_count in enumerate(list(map(int, read().split()))):
    for cnt in range(op_count):
        ops.append(operations[i])

vmin, vmax = 10 ** 9, -(10 ** 9)

for candidate in set(permutations(ops, len(ops))):
    eval_string = nums[0]
    idx = 1
    for op in candidate:
        eval_string += op + nums[idx]
        idx += 1
        eval_string = str(int(eval(eval_string)))

    vmin = min(vmin, int(eval_string))
    vmax = max(vmax, int(eval_string))

print(vmax)
print(vmin)
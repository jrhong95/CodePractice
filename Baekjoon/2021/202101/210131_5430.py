import sys
from collections import deque
read = sys.stdin.readline


def solution():
    commands = list(read().rstrip())
    _ = int(read())
    nums = read().strip('[]\n')
    nums = deque(nums.split(',')) if nums else []

    is_reversed = False
    for command in commands:
        if command == 'R':
            is_reversed = not is_reversed
        elif command == 'D':
            if nums:
                if is_reversed:
                    nums.pop()
                else:
                    nums.popleft()
            else:
                return 'error'

    if is_reversed:
        nums.reverse()
    return f'[{",".join(nums)}]'


for _ in range(int(read())):
    print(solution())

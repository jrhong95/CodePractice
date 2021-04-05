# bfs
def solution(numbers, target):
    from collections import deque

    queue = deque()
    queue.append((0, 0))
    ans = 0

    while queue:
        cur_sum, cur_idx = queue.popleft()

        if cur_idx == len(numbers) and cur_sum == target:
            ans += 1
        elif cur_idx < len(numbers):
            queue.append((cur_sum + numbers[cur_idx], cur_idx + 1))
            queue.append((cur_sum - numbers[cur_idx], cur_idx + 1))

    return ans


def solution2(numbers, target):
    from itertools import product

    nums = list(map(lambda x: (-x, x), numbers))
    ans = list(map(sum, product(*nums))).count(target)

    return ans


print(solution2([1, 1, 1, 1, 1], 3))

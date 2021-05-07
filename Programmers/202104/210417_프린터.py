priority_count = [0] * 10


def check(n):
    if n == 9:
        return True
    for i in range(n + 1, 10):
        if priority_count[i] > 0:
            return False
    return True


def solution(priorities, location):
    new_priority = []
    for i, p in enumerate(priorities):
        priority_count[p] += 1
        new_priority.append((p, i))

    answer = 0
    while new_priority:
        n, i = new_priority.pop(0)
        if not check(n):
            new_priority.append((n, i))
        else:
            priority_count[n] -= 1
            answer += 1

            if i == location:
                return answer


print(solution([2, 1, 3, 2], 2))

from functools import cmp_to_key


def compare(a, b):
    if int(a + b) < int(b + a):
        return 1
    elif int(a + b) > int(b + a):
        return -1
    else:
        return 0


def solution(numbers):
    numbers = sorted([str(i) for i in numbers], key=cmp_to_key(compare))
    return str(int("".join(numbers)))


print(solution([6, 10, 2]))
print(solution([6, 10, 2, 0]))
print(solution([0, 0, 0]))
print(solution([3, 30, 34, 5, 9]))
print(solution([341, 41, 94, 940, 9]))

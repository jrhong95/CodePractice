from itertools import combinations


def solution(numbers):
    return list(set(map(sum, combinations(numbers, 2))))


print(solution([5, 0, 2, 7]))

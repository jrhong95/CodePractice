def solution(n, lost, reserve):
    students = [1] * (n + 1)

    for l in lost:
        students[l] -= 1

    for r in reserve:
        students[r] += 1

    for i in range(1, n + 1):
        if students[i] == 0:
            if i > 1 and students[i - 1] > 1:
                students[i - 1] -= 1
                students[i] += 1
            elif i < n and students[i + 1] > 1:
                students[i + 1] -= 1
                students[i] += 1

    return sum(s > 0 for s in students[1:])

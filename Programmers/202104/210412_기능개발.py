import math


def solution(progresses, speeds):
    ans = []
    days = [math.ceil((100 - progress) / speed) for progress,
            speed in zip(progresses, speeds)]
    print(days)
    count, max_day = 1, days[0]
    for day in days[1:]:
        if day <= max_day:
            count += 1
        else:
            ans.append(count)
            max_day = day
            count = 1
    ans.append(count)
    return ans


print(solution([93, 30, 55], [1, 30, 5]))  # 7, 3, 9
# 5, 10, 1, 1, 20, 1
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 100, 1, 1]))

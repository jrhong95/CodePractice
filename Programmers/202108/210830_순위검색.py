from itertools import combinations
from collections import defaultdict
from bisect import bisect_left


def solution(informations, queries):
    info_dict = defaultdict(list)
    answer = []

    for info in informations:
        info = info.split()
        condition = info[:-1]
        score = int(info[-1])

        for n in range(5):
            for candidate in combinations(range(4), n):
                tmp_cond = condition[:]
                for i in candidate:
                    tmp_cond[i] = "-"
                info_dict[tuple(tmp_cond)].append(score)

    for key in info_dict:
        info_dict[key].sort()

    query = [q.split(" and ") for q in queries]
    for q in query:
        q.extend(q.pop().split())

        query_cond = tuple(q[:-1])
        query_score = int(q[-1])

        if query_cond in info_dict:
            count_start = bisect_left(info_dict[query_cond], query_score)
            answer.append(len(info_dict[query_cond]) - count_start)
        else:
            answer.append(0)

    return answer


print(
    solution(
        [
            "java backend junior pizza 150",
            "python frontend senior chicken 210",
            "python frontend senior chicken 150",
            "cpp backend senior pizza 260",
            "java backend junior chicken 80",
            "python backend senior chicken 50",
        ],
        [
            "java and backend and junior and pizza 100",
            "python and frontend and senior and chicken 200",
            "cpp and - and senior and pizza 250",
            "- and backend and senior and - 150",
            "- and - and - and chicken 100",
            "- and - and - and - 150",
        ],
    )
)

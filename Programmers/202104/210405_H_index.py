from collections import Counter


def solution(citations):
    dic = sorted(Counter(citations).items(), key=lambda x: x[0])

    l, i = len(citations), 0
    new_dic = []

    while l > 0:
        new_dic.append([dic[i][0], l])
        l -= dic[i][1]

        if new_dic[i][0] >= new_dic[i][1]:
            return new_dic[i][1]
        i += 1

    return 0

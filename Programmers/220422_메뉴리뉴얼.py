from itertools import combinations
from collections import Counter


def solution(orders, course):
    ans = []
    for c in course:
        combs = Counter()
        for order in orders:
            combs += Counter(
                map(lambda x: "".join(sorted(x)), list(combinations(order, c)))
            )
        combs = combs.most_common()
        ans += [menu for menu, cnt in combs if cnt > 1 and cnt == combs[0][1]]
    return sorted(ans)
def solution(weights, head2head):
    infos = []

    for i, fight in enumerate(head2head):
        win, win_over_weight, total = 0, 0, 0
        for j in range(len(fight)):
            if i == j or fight[j] == "N":
                continue
            total += 1
            if fight[j] == "W":
                win += 1
                if weights[i] < weights[j]:
                    win_over_weight += 1
        infos.append((win / total if total else 0, win_over_weight, weights[i], i + 1))

    return [p[3] for p in sorted(infos, key=lambda x: (-x[0], -x[1], -x[2], x[3]))]
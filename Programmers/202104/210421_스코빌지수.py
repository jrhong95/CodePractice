from heapq import heapify, heappop, heappush


def solution(scoville, K):
    heapify(scoville)
    mix = 0

    while scoville:
        s1 = heappop(scoville)
        if s1 >= K:
            return mix
        elif not scoville:
            return -1

        heappush(scoville, s1 + heappop(scoville) * 2)
        mix += 1

    return -1


print(solution([1, 2, 3, 9, 10, 12], 7))

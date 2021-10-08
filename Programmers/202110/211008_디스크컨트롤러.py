from heapq import *


def solution(jobs):
    l = len(jobs)
    disk_heap = []
    heapify(jobs)
    time_sum, now = 0, 0

    while jobs or disk_heap:
        while jobs and jobs[0][0] <= now:
            start, due = heappop(jobs)
            heappush(disk_heap, (due, start))

        if disk_heap:
            due, start = heappop(disk_heap)
            time_sum += now + due - start
            now += due
        else:
            now += 1

    return time_sum // l
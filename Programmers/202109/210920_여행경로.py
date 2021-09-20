from collections import defaultdict


def solution(tickets):
    answer = []
    size = len(tickets) + 1
    graph = defaultdict(list)

    for s, d in tickets:
        graph[s].append(d)
    for k in graph:
        graph[k].sort(reverse=True)

    stack = ["ICN"]

    while stack:
        top = stack[-1]
        if not graph[top]:
            answer.append(stack.pop())
        else:
            stack.append(graph[top].pop())

    return answer[::-1]
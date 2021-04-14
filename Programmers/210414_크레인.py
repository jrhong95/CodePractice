from collections import deque


def solution(board, moves):
    queues = [deque() for _ in range(len(board))]
    for line in board:
        for i, n in enumerate(line):
            if n:
                queues[i].appendleft(n)

    stack, count = [], 0
    for move in moves:
        if queues[move - 1]:
            n = queues[move - 1].pop()
            if stack and stack[-1] == n:
                stack.pop()
                count += 1
            else:
                stack.append(n)

    return count * 2

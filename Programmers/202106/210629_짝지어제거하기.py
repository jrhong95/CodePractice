from collections import deque


def solution(s):
    s = deque(s)
    stack = []

    while s:
        cur = s.popleft()

        if stack and stack[-1] == cur:
            stack.pop()
        else:
            stack.append(cur)

    return 0 if stack else 1
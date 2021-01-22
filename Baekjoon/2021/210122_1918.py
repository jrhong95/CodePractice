import sys
from collections import deque
read = sys.stdin.readline

stack = []
answer = ""

for c in read().rstrip():
    if c in "*/":
        while stack and stack[-1] in "*/":
            answer += stack.pop()
        stack.append(c)
    elif c in "+-":
        while stack and stack[-1] != "(":
            answer += stack.pop()
        stack.append(c)
    elif c in "()":
        if c == "(":
            stack.append(c)
        else:
            while stack and stack[-1] != "(":
                answer += stack.pop()
            stack.pop()
    else:
        answer += c

while stack:
    answer += stack.pop()
print(answer)

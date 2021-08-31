import sys
from collections import deque

read = sys.stdin.readline

N = int(read())
queue = deque()

for _ in range(N):
    command = read().rstrip().split()

    if command[0] == "push":
        queue.append(command[1])
    elif command[0] == "pop":
        print(queue.popleft() if len(queue) else -1)
    elif command[0] == "size":
        print(len(queue))
    elif command[0] == "empty":
        print(0 if len(queue) else 1)
    elif command[0] == "front":
        print(queue[0] if len(queue) else -1)
    elif command[0] == "back":
        print(queue[-1] if len(queue) else -1)

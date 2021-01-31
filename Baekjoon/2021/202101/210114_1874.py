import sys
from collections import deque
read = sys.stdin.readline


arr = deque([n + 1 for n in range(int(read()))])
stack = deque()
out = []


for _ in range(len(arr)):
    num = int(read())

    if arr and arr[0] <= num:
        while arr and arr[0] <= num:
            stack.append(arr.popleft())
            out.append('+')

        stack.pop()
        out.append('-')

    else:
        if stack[-1] == num:
            stack.pop()
            out.append('-')
        else:
            out = []
            break

if not out:
    print("NO")
else:
    print(*out, sep='\n')

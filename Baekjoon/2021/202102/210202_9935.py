import sys
read = sys.stdin.readline

S = read().rstrip()
boom = read().rstrip()

stack = []

for c in S:
    flag = True
    stack.append(c)

    if stack[-1] == boom[-1] and len(stack) >= len(boom):
        for i in range(-1, -len(boom) - 1, -1):
            if stack[i] != boom[i]:
                flag = False
                break
        if flag:
            boom_length_check = 0
            while boom_length_check < len(boom):
                stack.pop()
                boom_length_check += 1

print("".join(stack) if stack else "FRULA")

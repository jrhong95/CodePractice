import sys
read = sys.stdin.readline


line = read().rstrip()

while line != '.':
    stack = []

    for c in line:
        if c == '(' or c == '[':
            stack.append(c)
        elif c == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(c)
                break
        elif c == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(c)
                break
    print("no" if stack else "yes")

    line = read().rstrip()

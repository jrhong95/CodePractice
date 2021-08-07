import sys

read = sys.stdin.readline

stack = []

for i in read().rstrip():

    if i == ")":
        tmp = 0

        while stack:
            top = stack.pop()
            if top == "(":
                stack.append(2 * tmp if tmp else 2)
                break
            elif top == "[":
                print(0)
                exit(0)
            else:
                tmp = top + tmp if tmp else top

    elif i == "]":
        tmp = 0

        while stack:
            top = stack.pop()
            if top == "[":
                stack.append(3 * tmp if tmp else 3)
                break
            elif top == "(":
                print(0)
                exit(0)
            else:
                tmp = top + tmp if tmp else top

    else:
        stack.append(i)

if "(" in stack or "[" in stack:
    print(0)
else:
    print(sum(stack))

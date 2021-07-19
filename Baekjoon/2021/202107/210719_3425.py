import sys

read = sys.stdin.readline
MAX_NUMBER = 10 ** 9


def num_x(stack, x):
    stack.append(x)
    return True


def pop(stack):
    if stack:
        stack.pop()
        return True
    else:
        return False


def inv(stack):
    if stack:
        stack.append(-stack.pop())
        return True
    else:
        return False


def dup(stack):
    if stack:
        stack.append(stack[-1])
        return True
    else:
        False


def swp(stack):
    if len(stack) > 1:
        n1 = stack.pop()
        n2 = stack.pop()

        stack.append(n1)
        stack.append(n2)
        return True
    else:
        return False


def add(stack):
    if len(stack) > 1:
        n1 = stack.pop()
        n2 = stack.pop()

        if n1 + n2 > MAX_NUMBER:
            return False

        stack.append(n1 + n2)
        return True
    else:
        return False


def sub(stack):
    if len(stack) > 1:
        n1 = stack.pop()
        n2 = stack.pop()

        if abs(n2 - n1) > MAX_NUMBER:
            return False

        stack.append(n2 - n1)
        return True
    else:
        return False


def mul(stack):
    if len(stack) > 1:
        n1 = stack.pop()
        n2 = stack.pop()

        if abs(n1 * n2) > MAX_NUMBER:
            return False

        stack.append(n1 * n2)
        return True
    else:
        return False


def div(stack):
    if len(stack) > 1:
        n1 = stack.pop()
        n2 = stack.pop()

        if n1 == 0:
            return False
        stack.append(int(n2 / n1))
        return True
    else:
        return False


def mod(stack):
    if len(stack) > 1:
        n1 = stack.pop()
        n2 = stack.pop()

        if n1 == 0:
            return False
        ans = abs(n2) % abs(n1)

        if n2 < 0:
            stack.append(-ans)
        else:
            stack.append(ans)
        return True
    else:
        return False


def execute_commands(commands, number):
    stack = [number]
    for command in commands:
        command = command.split(" ")

        if command[0] == "NUM":
            if not num_x(stack, int(command[1])):
                return "ERROR"
        elif command[0] == "POP":
            if not pop(stack):
                return "ERROR"
        elif command[0] == "INV":
            if not inv(stack):
                return "ERROR"
        elif command[0] == "DUP":
            if not dup(stack):
                return "ERROR"
        elif command[0] == "SWP":
            if not swp(stack):
                return "ERROR"
        elif command[0] == "ADD":
            if not add(stack):
                return "ERROR"
        elif command[0] == "SUB":
            if not sub(stack):
                return "ERROR"
        elif command[0] == "MUL":
            if not mul(stack):
                return "ERROR"
        elif command[0] == "DIV":
            if not div(stack):
                return "ERROR"
        elif command[0] == "MOD":
            if not mod(stack):
                return "ERROR"

    return stack.pop() if len(stack) == 1 else "ERROR"


while True:
    command_list = []
    command = read().rstrip()

    if command == "QUIT":
        break
    elif command == "":
        continue
    else:
        while command != "END":
            command_list.append(command)
            command = read().rstrip()

        nums = [int(read()) for _ in range(int(read()))]

        for num in nums:
            print(execute_commands(command_list, num))
        print("")

def check_correct(string):
    stack = []
    while string:
        cur = string.pop(0)
        if not stack:
            stack.append(cur)
        elif stack and stack[-1] == "(" and cur == ")":
            stack.pop()
        else:
            stack.append(cur)

    return False if stack else True


def split_string(string):
    check = {"(": 0, ")": 0}
    u = ""
    while string:
        cur = string.pop(0)
        check[cur] += 1
        u += cur
        if check["("] == check[")"]:
            break

    return u, "".join(string)


def solution(p):
    if p:
        u, v = split_string(list(p))

        if check_correct(list(u)):
            return u + solution(v)
        else:
            tmp = f"({solution(v)})"

            for c in u[1:-1]:
                if c == "(":
                    tmp += ")"
                else:
                    tmp += "("
            return tmp

    else:
        return ""
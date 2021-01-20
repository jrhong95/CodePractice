import sys
read = sys.stdin.readline

answer = ""


def check_data(new_data):
    color = new_data[0][0]
    length = len(new_data)
    for i in range(length):
        for j in range(length):
            if color != new_data[i][j]:
                return -1
    return color


def cut(data):
    global answer
    check = check_data(data)

    if check == -1:
        length = len(data)
        divide = length // 2
        answer += "("

        for i in range(0, length, divide):
            for j in range(0, length, divide):
                next_paper = [data[row][0 + j: divide + j]
                              for row in range(0 + i, divide + i)]
                cut(next_paper)

        answer += ")"

    else:
        answer += str(check)


N = int(read())
origin_data = [list(map(int, list(read().rstrip()))) for _ in range(N)]
cut(origin_data)

print(answer)

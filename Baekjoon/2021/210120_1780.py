import sys
read = sys.stdin.readline

answer = [0, 0, 0]


def check_color(paper):
    color = paper[0][0]
    length = len(paper)
    for i in range(length):
        for j in range(length):
            if color != paper[i][j]:
                return -2
    return color


def cut(paper):
    global answer
    check = check_color(paper)

    if check == -2:
        length = len(paper)
        divide = length // 3

        for i in range(0, length, divide):
            for j in range(0, length, divide):
                next_paper = [paper[row][0 + j: divide + j]
                              for row in range(0 + i, divide + i)]
                cut(next_paper)

    else:
        answer[check + 1] += 1


N = int(read())
paper = [list(map(int, read().split())) for _ in range(N)]
cut(paper)

print(*answer, sep='\n')

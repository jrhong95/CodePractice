import sys
read = sys.stdin.readline

white, blue = 0, 0

def check_color(paper):
    color = paper[0][0]
    for i in range(len(paper)):
        for j in range(len(paper)):
            if color != paper[i][j]:
                return  -1
    return color

def cut(paper):
    global white, blue
    check = check_color(paper)

    if check == -1:
        half = len(paper) // 2

        for i in [0, half]:
            for j in [0, half]:
                cut([paper[row][0 + j : half + j] for row in range(0 + i, half + i)])
    
    else:
        if check == 0:
            white += 1
        else:
            blue += 1



N = int(read())
paper = [list(map(int, read().split())) for _ in range(N)]
cut(paper)

print(white)
print(blue)

dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]


def solution(places):
    answer = []

    for place in places:
        place = [list(line) for line in place]
        flag = False
        for r in range(5):
            for c in range(5):
                if place[r][c] == "P":
                    place[r][c] = "O"
                    if not dfs(2, r, c, place):
                        answer.append(0)
                        flag = True
                        break
                    place[r][c] = "P"

            if flag:
                break
        else:
            answer.append(1)

    return answer


def dfs(count, r, c, place):
    if count < 2 and place[r][c] == "P":
        return False

    if count == 0:
        return True

    for i in range(4):
        cr = r + dr[i]
        cc = c + dc[i]

        if not 0 <= cr < 5 or not 0 <= cc < 5 or place[cr][cc] == "X":
            continue

        if not dfs(count - 1, cr, cc, place):
            return False

    return True
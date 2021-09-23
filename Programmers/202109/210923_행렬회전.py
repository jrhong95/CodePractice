dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def rotation(query):
    global matrix
    ret = 10 ** 6
    r1, c1, r2, c2 = map(lambda x: x - 1, query)
    cr, cc = r1, c1
    tmp = matrix[cr][cc]
    for i in range(4):
        nr = dr[i] + cr
        nc = dc[i] + cc
        while True:
            if not r1 <= nr <= r2 or not c1 <= nc <= c2:
                break
            ret = min(ret, tmp)
            matrix[nr][nc], tmp = tmp, matrix[nr][nc]
            cr, cc = nr, nc
            nr += dr[i]
            nc += dc[i]
    return ret


def solution(rows, columns, queries):
    global matrix
    matrix = [[i * columns + j + 1 for j in range(columns)] for i in range(rows)]
    return [rotation(query) for query in queries]
# 1011번 Fly me to the Alpha Centauri
for _ in range(int(input())):
    start, end = map(int, input().split())
    j, j_cnt, distance = 1, 0, end - start

    while distance - j * 2 >= 0:
        distance = distance - j * 2
        j_cnt += 2
        j += 1
    if distance != 0:
        j_cnt += distance // (j + 1) + 1

    print(j_cnt)
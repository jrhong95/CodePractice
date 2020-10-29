wh = []

for _ in range(int(input())):
    w, h = map(int, input().split())
    wh.append((w, h))

for i in range(len(wh)):
    cnt = 1
    for j in range(len(wh)):
        if wh[i][0] < wh[j][0] and wh[i][1] < wh[j][1]:
            cnt += 1
    print(cnt, end=' ')
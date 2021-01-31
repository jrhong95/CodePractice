N, y, x = map(int, input().split())
cnt = 0
row, col = False, False
max_row, max_col = pow(2, N), pow(2, N)

for i in range(N - 1, -1, -1):
    max_row = pow(2, i) + max_row if row else max_row - pow(2, i)
    max_col = pow(2, i) + max_col if col else max_col - pow(2, i)

    if max_col > x:
        col = False
        if max_row > y:
            mul, row = 0, False
        else:
            mul, row = 2, True
    else:
        col = True
        if max_row > y:
            mul, row = 1, False
        else:
            mul, row = 3, True

    cnt += pow(2, i) * pow(2, i) * mul
print(cnt)
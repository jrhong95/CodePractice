N, M = map(int, input().split())
board = [input() for _ in range(N)]

min_draw = N * M

for y in range(N - 7):
    for x in range(M - 7):
        cut_board = []
        for i in range(y, y + 8):
            cut_board.append(board[i][x : x + 8])
    
        start_black, start_white = 0, 0
        for i, line in enumerate(cut_board):
            for j, c in enumerate(line):
                if (i + j) % 2: # 홀수
                    if c == 'W':
                        start_white += 1
                    else:
                        start_black += 1
                else:           # 짝수
                    if c == 'W':
                        start_black += 1
                    else:
                        start_white += 1
        
        if min_draw > min(start_black, start_white):
            min_draw = min(start_black, start_white)

print(min_draw)
import sys
read = sys.stdin.readline

table = sorted([tuple(map(int, read().split())) for _ in range(int(read()))], key=lambda x: (x[1], x[0]))

count = 0
start = 0
for time in table:
    if time[0] >= start:
        count += 1
        start = time[1]

print(count)
import sys
read = sys.stdin.readline

K, N = map(int, read().split())
total_length = 0
lans = []
for _ in range(K):
    lan = int(read())
    lans.append(lan)
    total_length += lan

start, end = 1, total_length // N

while start <= end:
    mid = (start + end) // 2
    count = sum(lan // mid for lan in lans)

    if count >= N:
        start = mid + 1
    else:
        end = mid - 1

print(end)

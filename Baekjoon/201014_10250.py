# 10250번 ACM호텔
num = int(input())


for _ in range(num):
    H, W, N = map(int, input().split())
    room_cnt, floor = divmod(N, H)
    if floor == 0:
        floor = H
        room_cnt -= 1
    print(floor * 100 + room_cnt + 1)
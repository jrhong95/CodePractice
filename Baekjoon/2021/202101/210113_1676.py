N = int(input())
facto = [0] * 501
facto[0], facto[1] = 1, 1

if facto[N] == 0:
    for i in range(2, N + 1):
        facto[i] = i * facto[i - 1]

count = 0
while facto[N] % 10 == 0:
    facto[N] //= 10
    count += 1
print(count)

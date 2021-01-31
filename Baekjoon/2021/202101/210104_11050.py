facto = [1,1,2]
for i in range(3, 11):
    facto.append(facto[i-1] * i)

N, K = map(int, input().split())
print(facto[N] // (facto[K] * facto[N-K]))

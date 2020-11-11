import sys


c = [0] * 8001
max_cnt, max_idx = 0, 0 
for i in range(int(sys.stdin.readline())):
    idx = 4000 + int(sys.stdin.readline())
    c[idx] += 1
    if c[idx] > max_cnt:
        max_cnt = c[idx]
        max_idx = idx - 4000

l = []
for idx, n in enumerate(c):
    l.extend(idx - 4000 for _ in range(n))

print(round(sum(l) / len(l)))
print(l[len(l) // 2])

if c.count(max_cnt) == 1:
    print(max_idx)
else:
    cnt = 0
    for i, n in enumerate(c):
        if n == max_cnt:
            cnt += 1
        if cnt == 2:
            print(i - 4000)
            break

print(l[-1] - l[0])
from sys import stdin

l = []
for i in range(int(stdin.readline())):
    tmp = list(map(str, stdin.readline().split()))
    l.append([i, int(tmp[0]), tmp[1]])

l.sort(key=lambda x: (x[1], x[0]))
for a in l:
    print(a[1], a[2])
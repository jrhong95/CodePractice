n = int(input())
m = n
for a in range(n):
    s = a + sum(int(i) for i in str(a))
    if s == n and m >= a:
        m = a
print(m if m != n else 0)
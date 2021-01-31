import sys
read = sys.stdin.readline
a = list(read().rstrip().split('-'))

cal = sum(int(n) for n in a[0].split('+'))
for n in a[1:]:
    if '+' in n:
        cal -= sum(map(int, n.split('+')))
    else:
        cal -= int(n)
print(cal)

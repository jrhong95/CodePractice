import sys
read = sys.stdin.readline

n, k = map(int, read().split())
z = n
while bin(n).count('1') > k:
    n += n & -n
print(n-z)

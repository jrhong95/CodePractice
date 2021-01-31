import sys
read = sys.stdin.readline

N = int(read())

peoples = sorted(list(map(int, read().split())))
print(sum(sum(peoples[0:i]) for i in range(N + 1)))

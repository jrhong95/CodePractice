import sys
read = sys.stdin.readline

N, M = map(int, read().split())
pokemon = {}
poke = []
for i in range(N):
    a = read().rstrip()
    pokemon[a] = i
    poke.append(a)

for _ in range(M):
    a = read().rstrip()
    
    if a.isdigit():
        print(poke[int(a) - 1])
    else:
        print(pokemon[a] + 1)
        

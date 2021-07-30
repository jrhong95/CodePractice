import sys

MAX = 1000000
read = sys.stdin.readline
checks = [True, True] + [False for _ in range(2, MAX)]
primes = []
for i in range(2, MAX):
    if not checks[i]:
        primes.append(i)

        for j in range(i + i, MAX, i):
            checks[j] = True

while True:
    N = int(read())

    if N == 0:
        break

    for prime in primes:
        if prime >= N:
            print("Goldbach's conjecture is wrong.")
            break
        if not checks[N - prime]:
            print(f"{N} = {prime} + {N - prime}")
            break
import sys
read = sys.stdin.readline
BIG_PRIME_NUMBER = 1234567891

N = int(read())
S = read().rstrip()
print(sum((ord(S[i]) - 96) * (31 ** i) for i in range(N)) % BIG_PRIME_NUMBER)

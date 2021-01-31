def check(num):
    for n in list(str(num)):
            if int(n) in wrong_number:
                return False
    return True

N = int(input())
w = int(input())

if w != 0:
    wrong_number = list(map(int, input().split()))

if N == 100:
    print(0)
elif w == 0:
    print(len(str(N)) if len(str(N)) < abs(N - 100) else abs(N - 100))
elif w == 10:
    print(abs(N - 100))
else:
    count = abs(N - 100)
    for i in range(1000001):
        if check(i):
            count = min(count, abs(N - i) + len(str(i)))
    print(count)
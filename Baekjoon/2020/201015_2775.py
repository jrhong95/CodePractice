# 2775번 부녀회장이 될테야
T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())
    apt = [i + 1 for i in range(n)]
    for ki in range(k):
        for ni in range(1, n):
            apt[ni] += apt[ni - 1]
    print(apt[n - 1])
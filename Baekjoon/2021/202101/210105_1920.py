def binary_search(num):
    start, end = 0, N - 1
    while start <= end:
        mid = (start + end) // 2
        if n == A[mid]:
            return True
        elif n > A[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return False

N = int(input())
A = sorted(list(map(int, input().split())))
M = int(input())
num = list(map(int, input().split()))


for n in num:
    print(1 if binary_search(n) else 0)
    

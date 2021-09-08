import sys

read = sys.stdin.readline


def main():
    N = int(read())
    nums = list(map(int, read().split()))
    nums.sort(key=abs, reverse=True)

    zero_close = sys.maxsize
    ans = []
    for i in range(N - 1):
        a1, a2 = nums[i], nums[i + 1]
        if abs(a1 + a2) < abs(zero_close):
            zero_close = a1 + a2
            ans = [a1, a2]
    print(*sorted(ans), sep=" ")


main()
import sys
read = sys.stdin.readline

N = int(read())
nums = list(map(int, read().split()))
dic = {n: i for i, n in enumerate(sorted(set(nums)))}

print(" ".join(str(dic[n]) for n in nums))

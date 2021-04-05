import sys
from collections import defaultdict
read = sys.stdin.readline

for _ in range(int(read())):
    dic = defaultdict(list)

    for _ in range(int(read())):
        cloth, kind = read().rstrip().split()
        dic[kind].append(cloth)

    ans = 1
    for item in dic.values():
        ans *= len(item) + 1
    print(ans - 1)

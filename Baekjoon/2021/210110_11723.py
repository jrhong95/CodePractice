import sys
input = sys.stdin.readline

S = set()
one_to_20 = set(i for i in range(1, 21))
for _ in range(int(input())):
    command = input().split()

    if command[0] == 'all':
        S = one_to_20
    elif command[0] == 'empty':
        S = set()
    elif command[0] == 'add':
        S.add(int(command[1]))
    elif command[0] == 'remove' and int(command[1]) in S:
        S.remove(int(command[1]))
    elif command[0] == 'check':
        print(1 if int(command[1]) in S else 0)
    elif command[0] == 'toggle':
        if int(command[1]) in S:
            S.remove(int(command[1]))
        else:
            S.add(int(command[1]))

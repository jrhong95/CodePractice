import sys

read = sys.stdin.readline


def key_exist(person, idx):
    try:
        value = people[person]
    except KeyError:
        return False
    return True


def find(a):
    if parent[a] == a:
        return a
    tmp = find(parent[a])
    parent[a] = tmp
    return parent[a]


def union(a, b):
    a, b = find(a), find(b)

    if a != b:
        parent[a] = b
        friend_count[b] += friend_count[a]
        friend_count[a] = 1
    return friend_count[b]


def main():
    global people, parent, friend_count
    ans = []
    for _ in range(int(read())):
        F = int(read())
        people = dict()
        parent = [i for i in range(F * 2)]
        friend_count = [1] * (F * 2)
        idx = 0

        for __ in range(F):
            p1, p2 = read().rstrip().split()
            if not key_exist(p1, idx):
                people[p1] = idx
                idx += 1
            if not key_exist(p2, idx):
                people[p2] = idx
                idx += 1
            ans.append(union(people[p1], people[p2]))

    print(*ans, sep="\n")


main()

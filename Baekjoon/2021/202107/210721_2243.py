import sys

read = sys.stdin.readline
FLAVOR_COUNT = 1000000


def init():
    global tree
    tree = [0] * 2 * S


def query(node, rank):
    if S <= node < 2 * S:
        return node - S + 1
    else:
        left_count = tree[node * 2]
        if rank <= left_count:
            return query(node * 2, rank)
        else:
            return query(node * 2 + 1, rank - left_count)


def update(left, right, node, target, diff):
    global tree
    if target < left or target > right:
        return
    else:
        tree[node] += diff
        if left != right:
            mid = (left + right) // 2
            update(left, mid, node * 2, target, diff)
            update(mid + 1, right, node * 2 + 1, target, diff)


def main():
    global S
    global tree
    S = 1
    tree = []

    while S < FLAVOR_COUNT:
        S *= 2

    init()
    ans = []
    for _ in range(int(read())):
        tc = list(map(int, read().split()))
        if tc[0] == 1:  # 사탕 가져오는 경우
            cur_candy = query(1, tc[1])
            update(1, S, 1, cur_candy, -1)
            print(cur_candy)
        else:  # 사탕 넣는 경우
            update(1, S, 1, tc[1], tc[2])


main()

import sys

read = sys.stdin.readline


class Node:
    def __init__(self):
        self.children = [None] * 10
        self.is_num = False


def set_trie(root: Node, numbers):
    for number in numbers:
        cur = root
        for n in number:
            n = int(n)
            if not cur.children[n]:
                cur.children[n] = Node()

            cur = cur.children[n]
        cur.is_num = True


def consistency(root: Node, numbers):
    for number in numbers:
        cur = root
        for i, n in enumerate(number):
            n = int(n)

            if cur.is_num and i <= len(number) - 1:
                return False
            else:
                cur = cur.children[n]
    return True


def main():
    for _ in range(int(read())):
        root = Node()
        numbers = [list(read().rstrip()) for __ in range(int(read()))]
        set_trie(root, numbers)
        print("YES" if consistency(root, numbers) else "NO")


main()

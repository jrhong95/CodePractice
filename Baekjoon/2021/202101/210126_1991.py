import sys
read = sys.stdin.readline

tree = {}


def preorder(node):
    print(node, end='')
    if tree[node][0] != '.':    # Left
        preorder(tree[node][0])
    if tree[node][1] != '.':
        preorder(tree[node][1])  # Right


def inorder(node):
    if tree[node][0] != '.':    # Left
        inorder(tree[node][0])
    print(node, end='')
    if tree[node][1] != '.':
        inorder(tree[node][1])  # Right


def postorder(node):
    if tree[node][0] != '.':    # Left
        postorder(tree[node][0])
    if tree[node][1] != '.':
        postorder(tree[node][1])  # Right
    print(node, end='')


N = int(read())
for _ in range(N):
    node, left, right = map(str, read().rstrip().split())
    tree[node] = [left, right]

preorder('1')
print()
inorder('1')
print()
postorder('1')

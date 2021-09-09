import sys

sys.setrecursionlimit(10 ** 6)


class Node:
    def __init__(self, node_list):
        self.data = node_list[0][2]

        left_list, right_list = [], []
        cur_data = node_list[0]

        for node in node_list[1:]:
            if cur_data[1] > node[1]:
                left_list.append(node)
            else:
                right_list.append(node)

        self.left = Node(left_list) if left_list else None
        self.right = Node(right_list) if right_list else None


def preorder(node):
    if not node:
        return
    pre.append(node.data)
    preorder(node.left)
    preorder(node.right)


def postorder(node):
    if not node:
        return
    postorder(node.left)
    postorder(node.right)
    post.append(node.data)


def solution(nodeinfo):
    global pre, post

    nodeinfo = [x + [i + 1] for i, x in enumerate(nodeinfo)]
    node_info = [[y, x, z] for x, y, z in sorted(nodeinfo, key=lambda x: (-x[1], x[0]))]

    root = Node(node_info)
    pre, post = [], []
    preorder(root)
    postorder(root)
    return [pre, post]
import sys
read = sys.stdin.readline
sys.setrecursionlimit(10**9)
N = int(read())

inorder = list(map(int, read().split()))
postorder = list(map(int, read().split()))
position = [0] * (N + 1)
for i in range(N):
    position[inorder[i]] = i


def divide(i_start, i_end, p_start, p_end):
    if i_start > i_end or p_start > p_end:
        return
    root = postorder[p_end]
    print(root, end=' ')
    inorder_root_idx = position[root]

    left = inorder_root_idx - i_start
    divide(i_start, inorder_root_idx - 1, p_start, p_start + left - 1)  # left
    divide(inorder_root_idx + 1, i_end, p_start + left, p_end - 1)  # right


divide(0, N - 1, 0, N - 1)

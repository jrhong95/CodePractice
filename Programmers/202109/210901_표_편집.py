class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


def solution(n, k, cmd):
    stack, sheet_size = [], n
    sheet = Node(0)
    cur = sheet

    for i in range(1, n):
        new_sheet = Node(i)
        cur.next = new_sheet
        new_sheet.prev = cur
        cur = new_sheet

    cnt, cur = 0, sheet
    while cnt < k:
        cur = cur.next
        cnt += 1

    for c in cmd:
        if c[0] == "U":
            for i in range(int(c[2:])):
                cur = cur.prev
                k -= 1
        elif c[0] == "D":
            for i in range(int(c[2:])):
                cur = cur.next
                k += 1
        elif c[0] == "C":
            stack.append(cur)
            if not cur.next:  # if tail
                k -= 1
                cur = cur.prev
                cur.next = None
            elif not cur.prev:  # if head
                cur = cur.next
                cur.prev = None
            else:
                cur.prev.next = cur.next
                cur.next.prev = cur.prev
                cur = cur.next
        elif c[0] == "Z":
            pop_node = stack.pop()
            if not pop_node.next:
                pop_node.prev.next = pop_node
            elif not pop_node.prev:
                pop_node.next.prev = pop_node
            else:
                pop_node.prev.next = pop_node
                pop_node.next.prev = pop_node

    ans = ["O"] * n
    for node in stack:
        ans[node.data] = "X"
    return "".join(ans)
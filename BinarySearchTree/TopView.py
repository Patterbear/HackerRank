from collections import deque


def topView(root):
    if not root:
        return

    hd_node_map = {}
    queue = deque([(root, 0)])

    min_hd = max_hd = 0

    while queue:
        node, hd = queue.popleft()

        if hd not in hd_node_map:
            hd_node_map[hd] = node.info
            min_hd = min(min_hd, hd)
            max_hd = max(max_hd, hd)

        if node.left:
            queue.append((node.left, hd - 1))
        if node.right:
            queue.append((node.right, hd + 1))

    for hd in range(min_hd, max_hd + 1):
        print(hd_node_map[hd], end=" ")

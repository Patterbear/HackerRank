from collections import deque


def levelOrder(root):
    if not root:
        return

    queue = deque([root])

    while queue:
        node = queue.popleft()
        print(node.info, end=" ")

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

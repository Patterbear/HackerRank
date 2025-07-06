# Iterative
def preOrder(root):
    stack = [root]
    while stack:
        node = stack.pop()
        print(node.info, end=" ")
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)


# Recursive
def preOrder(root):
    if not root:
        return
    print(root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)

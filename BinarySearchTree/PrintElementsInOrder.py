# Recursive
def inOrder(root):
    if not root:
        return
    inOrder(root.left)
    print(root.info, end=" ")
    inOrder(root.right)


# Iterative
def inOrder(root):
    stack = []
    current = root

    while stack or current:
        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()
        print(current.info, end=" ")
        current = current.right

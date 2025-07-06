def height(root):
    if not root:
        return -1

    left_height = height(root.left)
    right_height = height(root.right)

    if left_height > right_height:
        return 1 + left_height
    else:
        return 1 + right_height

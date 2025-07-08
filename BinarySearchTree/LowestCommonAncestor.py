def lca(root, v1, v2):
    if root is None:
        return None

    if root.info == v1 or root.info == v2:
        return root

    left_lca = lca(root.left, v1, v2)
    right_lca = lca(root.right, v1, v2)

    if left_lca and right_lca:
        return root

    if left_lca:
        return left_lca
    else:
        return right_lca

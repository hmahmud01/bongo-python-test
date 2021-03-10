# Least Common Ancestor problem
def lca(root, n1, n2):
    if root is None:
        return None

    if root.key == n1 or root.key == n2:
        return root

    right_lca = lca(root.right, n1, n2)
    left_lca = lca(root.left, n1, n2)

    if right_lca and left_lca:
        return root

    if left_lca is not None:
        return left_lca
    else:
        return right_lca
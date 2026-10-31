def height(root):
    # If using the edge-based definition, an empty tree returns -1
    if root is None:
        return -1

    return 1 + max(height(root.left), height(root.right))

print("Height:", height(root=None))

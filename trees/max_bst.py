def find_min(root):
    # Guard clause: handle an empty tree safely
    if root is None:
        return None  # Or raise an error / return a specific message

    while root.right:
        root = root.right

    return root.data

# Safe printing that checks if the tree was empty
max_val = find_min(root=None)
if max_val is not None:
    print("Maximum:", max_val)
else:
    print("The tree is empty.")

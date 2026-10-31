def find_min(root):
    # Guard clause: handle an empty tree safely
    if root is None:
        return None  # Or raise an error / return a specific message

    while root.left:
        root = root.left

    return root.data

# Safe printing that checks if the tree was empty
min_val = find_min(root=None)
if min_val is not None:
    print("Minimum:", min_val)
else:
    print("The tree is empty.")

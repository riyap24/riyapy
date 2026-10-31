# 1. Define the Node structure
class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

root = Node(50)
root.left = Node(30)
root.right = Node(70)

# 3. Your search function
def search(root, key):
    if root is None or root.data == key:
        return root

    if key < root.data:
        return search(root.left, key)

    return search(root.right, key)

# 4. Test the code
result = search(root, 30)

if result:
    print("Element found")      
    print("Element not found")

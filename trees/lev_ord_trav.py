from collections import deque

def level_order(root):
    # 1. Guard clause for empty trees
    if not root:
        return
        
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        print(node.data, end=" ")
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)



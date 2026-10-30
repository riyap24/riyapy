class node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
head = node(20)
head.next = node(30)

new_node = node(10)
new_node.next = head
head = new_node

current = head

while current:
    print(current.data, end="->")

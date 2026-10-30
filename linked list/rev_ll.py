class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

previous = None
current = head

while current:
    next_node = current.next
    current.next = previous
    previous = current
    current = next_node

head = previous

while head:
    print(head.data, end=" -> ")
    head = head.next
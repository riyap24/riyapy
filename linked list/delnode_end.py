class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

current = head

while current.next.next:
    current = current.next

current.next = None

while head:
    print(head.data, end=" -> ")
    head = head.next
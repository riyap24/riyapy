class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

head = Node(10)
second = Node(20)
third = Node(30)

head.next = second
second.prev = head

second.next = third
third.prev = second

current = head

while current:
    print(current.data, end=" <-> ")
    current = current.next
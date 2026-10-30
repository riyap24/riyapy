class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

key = 20
position = 1
found = False

current = head

while current:
    if current.data == key:
        print("Element found at position:", position)
        found = True
        break

    current = current.next
    position += 1

if not found:
    print("Element not found")
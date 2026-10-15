from collections import deque

queue = deque([10,20,30])

queue.append(40)
print("Queue:", queue)

queue.popleft()
print(" After dequeue:",queue)
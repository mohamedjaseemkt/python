from queue import Queue
my_queue = Queue()

my_queue.put(6)
my_queue.put(9)
my_queue.put(3)
my_queue.put(1)

print("Queue:",my_queue)

item =my_queue.get()
print("dequeue: ",item)

print("updated queue: ",my_queue.queue)


#stack
from collections import deque
my_stack = deque()

my_stack.append(7)
my_stack.append(5)
my_stack.append(3)
my_stack.append(8)

print("stack: ",my_stack)

item_ = my_stack.pop()
print("dequeue: ",item_)

print("updated stack: ",my_stack)

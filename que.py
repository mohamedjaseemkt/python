from queue import Queue

my_queue = Queue()

my_queue.put(1)
my_queue.put(2)
my_queue.put(3)

print("Queue:",my_queue.queue)

item = my_queue.get()
print("Dequeued item:",item)

print("updated Queue",my_queue.queue)

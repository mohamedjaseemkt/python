from queue import Queue
my_que = Queue()

my_que.put(3)
my_que.put(5)
my_que.put(7)
my_que.put(9)

print("Queue: ",my_que.queue)

item = my_que.get()
print("deleted item: ",item)

print("result: ",my_que.queue) 
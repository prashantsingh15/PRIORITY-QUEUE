from queue import Queue
q = Queue(maxsize = 3)
print(q.qsize())
q.put('a')
q.put('b')
q.put('c')

print("Prashant Singh")
print("2IES21CSE063")
print(q.full())
print("Elements dequeued from the queue")
print(q.get())
print(q.get())
print(q.get())

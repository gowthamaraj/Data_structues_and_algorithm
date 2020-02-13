"""
Queues can be implemented using various methods such as list, stack, and node
"""

class ListQueue:

    def __init__(self):
        self.queue = []
        self.size = 0

    def enqueue(self, data):
        self.queue.insert(0, data)
        self.size += 1

    def dequeue(self):
        data = self.queue.pop()
        self.size -= 1
        return data

q = ListQueue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)

print(q.dequeue())
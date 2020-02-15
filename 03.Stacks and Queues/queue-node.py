class Node(object):
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def enqueue(self, data):
        node = Node(data)
        if self.count == 0:
            self.head = node
            self.tail = node
            self.count += 1
        else:
            self.tail.next = node
            self.tail = node
            self.count += 1

    def dequeue(self):
        if self.count == 1:
            data = self.head.data
            self.head = None
            self.tail = None
            self.count = 0
            return data
        else:
            data = self.head.data
            self.head = self.head.next
            self.count -= 1
            return data

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)

print(q.dequeue())
print(q.dequeue())
q.enqueue(5)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
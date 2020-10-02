class Node():

    def __init__(self, data):
        self.data = data
        self.next = None


class Circular():

    def __init__(self):
        self.tail = None
        self.head = None
        self.size = 0

    def append(self, data):
        node = Node(data)
        if self.tail:
            self.tail.next = node
            self.tail = node
            self.tail.next = self.head
        else:
            self.tail = node
            self.head = node
        
        self.size += 1

    def iter(self):
        current = self.head
        for _ in range(self.size):
            yield(current)
            current = current.next

    def delete(self, data):
        prev = None
        for item in self.iter():
            if item.data == data:
                if item == self.head:
                    self.tail.next = item.next
                elif item == self.tail:
                    prev.next = self.head
                else:
                    prev.next = item.next
                self.size -= 1
            prev = item
    
    def __repr__(self):
        return ' '.join([item.data for item in self.iter()])

cl = Circular()
cl.append(1)
cl.append(2)
cl.append(3)
cl.append(4)
cl.delete(3)
for i in cl.iter():
    print(i.data)
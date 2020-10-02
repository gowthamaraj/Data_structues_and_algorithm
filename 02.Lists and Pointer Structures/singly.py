class Node:
    """
    single Node
    """
    def __init__(self, data= None):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

class SinglyLinkedList:
    """
    singly linked list
    """
    def __init__(self):
        self.tail = None
        self.head = None
        self.size = 0

    def append(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
            self.tail = self.head
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def iter(self):
        current = self.head
        while current:
            value = current.data 
            current = current.next
            yield(value)

    def delete(self, data):
        current = self.head
        prev = self.head
        while current:
            if current.data == data:
                if self.head.data == data:
                    self.head = self.head.next
                else:
                    prev.next = current.next
                self.size -= 1
                return
            prev = current
            current = current.next

    def search(self, data):
        for item in self.iter():
            if data == item.data:
                return True
        return False

    def __repr__(self):
        return self.head

s1 = SinglyLinkedList()
s1.append(1)
s1.append(2)
s1.append(3)
print([i for i in s1.iter()])
s1.delete(2)
print([i for i in s1.iter()])
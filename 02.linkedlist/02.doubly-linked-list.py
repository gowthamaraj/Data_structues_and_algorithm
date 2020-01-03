# https://stackabuse.com/doubly-linked-list-with-python-examples/

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

# Insert: inserts a new node into the list
# Size: returns size of list
# Search: searches list for a node containing the requested data and returns that node if found, otherwise None
# Delete: searches list for a node containing the requested data and removes it from list if found, otherwise return False

class DList:
    def __init__(self, head):
        node = Node(head)
        self.head = node
        self.tail = node

    def insert(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node

    def size(self):
        current = self.head
        count = 0
        while(current != None):
            count += 1
            current = current.next
        return count
    
    def search(self, data):
        if self.head == None:
            return None
        current = self.head
        while(current != None):
            if current.data == data:
                return current
            current = current.next
        return None

    def delete(self, data):
        current = self.head
        if current == None:
            return False
        if current.next == None:
            if current.data == data:
                self.head = None
                return True
            else:
                return False
        if current.data == data:
            self.head = current.next
            current.prev = None
            return True
        if self.tail.data == data:
            self.tail = self.tail.prev
            self.tail.next = None
            return True
        current = current.next
        while(current != None):
            if current.data == data:
                current.prev.next = current.next
                current.next.prev = current.prev
                current = current.next
                return True
        return False

# Testing
# Insertion operations
dlist = DList(1)
dlist.insert(2)
dlist.insert(3)
print(dlist.size())

# Search operation
print(dlist.search(1).data)

# delete operation
print(dlist.delete(3))
print(dlist.delete(1))
print(dlist.size())
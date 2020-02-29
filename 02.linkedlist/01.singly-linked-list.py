class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next

# The Linked List
# Insert: inserts a new node into the list
# Size: returns size of list
# Search: searches list for a node containing the requested data and returns that node if found, otherwise None
# Delete: searches list for a node containing the requested data and removes it from list if found, otherwise raises an error

class LinkedList:
    def __init__(self, head=None):
        node = Node(head)
        self.head = node
        self.tail = node

    def insert(self, data):
        node = Node(data)
        if self.head == None:
            self.head =  node
            self.tail = node
        else:
            self.tail.set_next(node)
            self.tail = node

    def size(self):
        current = self.head
        count = 0
        while(current != None):
            count += 1
            current = current.get_next()
        return count

    def search(self, data):
        if self.head == None:
            return None
        current = self.head
        while(current != None):
            if current.get_data() == data:
                return current
            current = current.get_next()
        return None

    def delete(self, data):
        current = self.head
        if current == None:
            return False
        if current.next == None:
            if current.get_data() == data:
                self.head = None
                return True
            else:
                return False
        if current.get_data() == data:
            self.head = current.get_next()
            return True
        previous = current
        current = current.get_next()
        while(current.get_next() != None):
            if current.get_data() == data:
                previous.set_next(current.get_next())
                return True
            current = current.get_next()
        return False

# Testing
# Insertion operations
LList = LinkedList(1)
LList.insert(2)
LList.insert(3)
print(LList.size())

# Search operation
print(LList.search(2).get_data())

# delete operation
print(LList.delete(4))
print(LList.size())
"""
Stacks can be implemented in Python using node.
"""

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Stack():
    def __init__(self):
        self.top = None
        self.next = None
        self.size = 0

    def push(self, data):
        node = Node(data)
        if self.top:
            node.next = self.top
            self.top = node
        else:
            self.top = node
        self.size += 1

    def pop(self):
        if self.size == 1:
            data = self.top.data
            self.top = None
            self.size = 0
            return data
        else:
            data = self.top.data
            self.top = self.top.next
            self.size -= 1
            return data

    def peek(self):
        return self.top.data


s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)

print(s.pop())
print(s.peek())
from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")
e = Node("E")
f = Node("F")
g = Node("G")
h = Node("H")

class Tree:
    def __init__(self, node):
        self.root = node

    def bft(self):
        list_of_nodes = []
        traversal_queue =  deque([self.root])
        while len(traversal_queue) > 0:
            node = traversal_queue.popleft()
            list_of_nodes.append(node.data)
            if node.left:
                traversal_queue.append(node.left)
            if node.right:
                traversal_queue.append(node.right)
        return list_of_nodes
        
a.left = b
a.right = c

c.right = f

b.left = d
b.right = e

d.left = g
d.right = h

T = Tree(a)
print(T.bft())
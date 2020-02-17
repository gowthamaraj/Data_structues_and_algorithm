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

    def postorder(self, root):
        current = root
        if current is None:
            return 
        self.postorder(root = current.left)
        self.postorder(root = current.right)
        print(current.data)


a.left = b
a.right = c

c.right = f

b.left = d
b.right = e

d.left = g
d.right = h

T = Tree(a)
T.postorder(a)
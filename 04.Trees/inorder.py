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

    def inorder(self, root):
        current = root
        if current is None:
            return 
        self.inorder(root = current.left)
        print(current.data)
        self.inorder(root = current.right)


a.left = b
a.right = c

c.right = f

b.left = d
b.right = e

d.left = g
d.right = h

T = Tree(a)
T.inorder(a)
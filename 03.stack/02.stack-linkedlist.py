# size()– Get the number of items in the stack.
# isEmpty() – Return True if the stack is empty, False otherwise.
# peek() – Return the top item in the stack.
# push(value) – Push a value into the head of the stack.
# pop() – Remove and return a value in the head of the stack. If the stack is empty, False

class Node:
   def __init__(self, data):
      self.data = data
      self.next = None

class Stack:
    def __init__(self):
        self.head = Node("head")
        self.size = 0

    def size(self):
        return self.size

    def isEmpty(self):
        return self.size() == 0

    def peek(self):
        if self.size() == 0:
            return None
        else:
            self.head.next.data
    
    def push(self, data):
        node = Node(data)
        node.next = self.head.next
        self.head.next = node
        self.size += 1

    def pop(self):
        if self.size > 0:
            node = self.head.next.next
            self.head.next = node
            return node.data
        else:
            return None

    def __str__(self):
      cur = self.head.next
      out = ""
      while cur:
         out += str(cur.data) + "->"
         cur = cur.next
      return out[:-2]

if __name__ == "__main__":
   stack = Stack()
   for i in range(1, 11):
      stack.push(i)
   print(f"Stack: {stack}")
 
   for _ in range(1, 6):
      remove = stack.pop()
      print(f"Pop: {remove}")
   print(f"Stack: {stack}")
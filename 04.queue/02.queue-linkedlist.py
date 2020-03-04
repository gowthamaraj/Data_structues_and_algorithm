class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = self.rear = None

    def isEmpty(self):
        return self.front == None

    def EnQueue(self, data):
        node = Node(data)
        if self.rear == None: 
            self.front = self.rear = node 
            return True
        self.rear.next = node 
        self.rear = node
        return True

    def DeQueue(self):
        if self.isEmpty(): 
            return False
        node = self.front
        self.front = node.next
        if(self.front == None): 
            self.rear = None
        return True

if __name__== '__main__': 
    q = Queue() 
    q.EnQueue(10) 
    q.EnQueue(20) 
    q.DeQueue() 
    q.DeQueue() 
    q.EnQueue(30) 
    q.EnQueue(40) 
    q.EnQueue(50)  
    q.DeQueue()    
    print("Queue Front " + str(q.front.data)) 
    print("Queue Rear " + str(q.rear.data)) 
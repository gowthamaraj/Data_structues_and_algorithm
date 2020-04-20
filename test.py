class Element(object):
    def __init__(self,value):
        self.value = value;
        self.next = None;

class Linkedlist(object):
    def __init__(self, head=None):
       self.head=head;

    def append(self, new_element):
        current = self.head;
        if self.head:
            while current.next:
                current = current.next;
            current.next= new_element;
        else:
            self.head=new_element;

    def get_position(self, position):

        if position < 1:
            return 0;

        else:
            current_ele = self.head;
            val = None;
            for i in range(position):
                if current_ele.next != None:
                    current_ele = current_ele.next;
            return current_ele.value;


    def insert(self, new_element, position):

        current_ele = self.head;
        position = position-1;
        while position:
            current_ele=current_ele.next;
            position = position-1;
        new_element.next = current_ele.next;
        current_ele.next = new_element;

        
    def delete(self, value):
        current = self.head
        previous = None
        while current.value != value and current.next:
            previous = current
            current = current.next
        if current.value == value:
            if previous:
                previous.next = current.next
            else:
                self.head = current.next

        
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = Linkedlist(e1)
ll.append(e2)
ll.append(e3)

# Test get_position
# Should print 3
print(ll.head.next.next.value)
# Should also print 3
print(ll.get_position(3))

# Test insert
ll.insert(e4,3)
# Should print 4 now
print(ll.get_position(3))

# Test delete
ll.delete(1)
# Should print 2 now
print(ll.get_position(1))
# Should print 4 now
print(ll.get_position(2))
# Should print 3 now
print(ll.get_position(3))






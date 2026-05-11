from cgi import test
from LinkedList import LinkedList, Node
class Stack:
    """Class representing a stack (LIFO) implemented using a linked list."""
    
    def __init__(self):
        """Initializes an empty stack."""
        self.list = LinkedList()
        self.number_of_elements = 0
    
    def is_empty(self):
        """Returns True if the stack is empty, otherwise False."""
        return self.list.is_empty()
    
    def __len__(self):
        """Returns the number of elements in the stack."""
        return self.number_of_elements
    
    def push(self, data):
        """Adds an element to the top of the stack."""
        self.list.insert_at_beginning(data)
        self.number_of_elements += 1
    
    def pop(self):
        """Removes the top element of the stack and returns data from it.
        Raises an error if the stack is empty.
        """
        if self.is_empty():
            raise ValueError("list is empty")
        vrchol = self.list.first()
        self.number_of_elements -= 1
        return self.list.remove_first()

    
    def top(self):
        """Returns data from the top element of the stack without removing it.
        Raises an error if the stack is empty.
        """
        return self.list.first()

class Stack1:
    """Class representing a stack (LIFO) implemented using Python array (class list)."""
    
    def __init__(self):
        """Initializes an empty stack."""
        self.list = []
    
    def is_empty(self):
        """Returns True if the stack is empty, otherwise False."""
        return self.list == []
    
    def __len__(self):
        """Returns the number of elements in the stack."""
        return len(self.list)
    
    def push(self, data):
        """Adds an element to the top of the stack."""
        self.list.append(data)
    
    def pop(self):
        """Removes the top element of the stack and returns data from it.
        Raises an error if the stack is empty.
        """
        if self.is_empty():
            raise ValueError("Cannot pop from empty stack.")
        data = self.list[-1]
        self.list.pop()
        return data
    
    def top(self):
        """Returns data from the top element of the stack without removing it.
        Raises an error if the stack is empty.
        """
        if self.is_empty():
            raise ValueError("Cannot top from empty stack.")
        return self.list[-1]

class Queue:
    """Class representing a queue (FIFO) implemented using a linked list."""
    
    def __init__(self):
        """Initializes an empty queue."""
        self.list = LinkedList()
        self.number_of_elements = 0
    
    def is_empty(self):
        """Returns True if the queue is empty, otherwise False."""
        return self.list.is_empty()
    
    def __len__(self):
        """Returns the number of elements in the queue."""
        return self.number_of_elements
    
    def enqueue(self, data): 
        """Adds an element to the end of the queue."""
        self.list.append(data)
        self.number_of_elements += 1
    
    def dequeue(self):
        """Removes the front element of the queue and returns data from it.
        Raises an error if the queue is empty.
        """
        if self.is_empty():
            raise ValueError("Cannot top from empty stack.")
        self.number_of_elements -= 1
        return self.list.remove_first()
    
    def front(self):
        """Returns data from the front element of the queue without removing it.
        Raises an error if the queue is empty.
        """
        return self.list.first()


def test_stack():
    s = Stack1()
    
    print("start:", len(s), s.is_empty())

    for x in range(10):
        s.push(x)
    
    print("after push:", len(s), s.is_empty())
    
    while not s.is_empty():
        print(s.top(), s.pop())

    print("end:", len(s), s.is_empty())

def test_queue():
    q = Queue()
    print("start:", len(q), q.is_empty())

    for x in range(10):
        q.enqueue(x)
    
    print("after enqueue:", len(q), q.is_empty())
    
    while not q.is_empty():
        print(q.front(), q.dequeue())

    print("end:", len(q), q.is_empty())

if __name__ == "__main__":
    test_stack()
    test_queue()

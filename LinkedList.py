from gettext import find
from turtle import heading

from sort import _rozdel


class Node:
    """Represents a node in a singly linked list."""
    def __init__(self, data=None): # None only if sentinel
        self.data = data # Data contained within the node
        self.next = None # Reference to the next node
        
    # alternatively: def __init__(self, data = None, next = None):
    
    def __str__(self) -> str:
        """Returns the string representation of the node (for printing)."""
        return str(self.data)


class LinkedList:
    """Represents a singly linked list with a sentinel node at the end (endnode).
    
    The sentinel node does not contain meaningful data and serves as a marker for the end of the list.


    The list supports two types of iterators:
    - LinkedListIterator (Python-style traversal)
    - PositionIterator (STL-like position representation)
    """
    
    def __init__(self):
        """Initializes an empty single linked list with a sentinel node (endnode)."""
        self.endnode = Node()
        self.head = self.endnode

    def is_empty(self) -> bool:
        """Returns True if the linked list is empty (i.e., contains only the sentinel node), False otherwise.
        """
        return self.head == self.endnode

    def append(self, data):
        """Appends a new node with the given data to the end of the linked list."""
        self.endnode.data = data
        new_endnode = Node(None)
        self.endnode.next = new_endnode
        self.endnode = new_endnode

    def insert_at_beginning(self, data):
        """Inserts a new node with the given data at the beginning of the linked list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def display(self):
        actual_node = self.head
        print("[]", end = "->")
        while actual_node != self.endnode:
            print(actual_node, end = " -> ")
            actual_node = actual_node.next
        print(".")

    def __str__(self) -> str:
        """Converts the LinkedList to string (for print): lists data from all nodes in the linked list."""
        actual_node = self.head
        s = "[] -> "
        while actual_node != self.endnode:
            s += str(actual_node) + " -> "
            actual_node = actual_node.next
        s += "."
        return s

    def delete_all(self):
        """Deletes all nodes from the linked list (except the sentinel node)."""
        self.head = self.endnode

    def find(self, data) -> Node | None:
        """
        Finds the first occurrence of a node with the specified data in the linked list.
        
        Returns:
            - The first node containing the specified data, if found.
            - None if no matching node is found.
        """
        current_node = self.head
        while True:
            if current_node == self.endnode:
                return None
            if current_node.data == data:
                return current_node
            current_node = current_node.next
        
    def first(self):
        """
        Returns the data stored in the first node of the linked list.
        
        Raises:
            ValueError: If the linked list is empty.
        """
        if self.is_empty():
            raise ValueError("list is empty")
        return self.head.data

    def last(self):
        """
        Returns the data stored in the last node of the linked list (the node before the sentinel node).
        
        Raises:
            ValueError: If the linked list is empty.
        """
        if self.is_empty():
            raise ValueError("list is empty")
        current_node = self.head.next
        while True:
            if current_node.next == self.endnode:
                return current_node.data
            current_node = current_node.next

    def remove_first(self):
        """
        Removes the first node of the linked list and returns the data from it.
        
        Raises:
            ValueError: If the linked list is empty.
        """
        if self.is_empty():
            raise ValueError("list is empty")
        data = self.head.data
        self.head = self.head.next
        return data

    def remove_last(self):
        """
        Removes the last node of the linked list and returns the data from it.
        
        Raises:
            ValueError: If the linked list is empty.
        """
        if self.is_empty():
            raise ValueError("list is empty")
        if self.head.next == self.endnode: #Linked list only has one Node
            return self.remove_first()
        current_node = self.head
        while True:
            if current_node.next == self.endnode:
                data = current_node.data
                current_node.next = None
                self.endnode = current_node
                return data
            current_node = current_node.next
            

    def delete(self, data) -> bool:
        """
        Deletes the first occurrence of a node with the specified data from the linked list.
        
        Returns:
            bool: True if a node was deleted, False if the data was not found.
        """
        current_node = self.head
        while True:
            if current_node == self.endnode:
                return False
            if current_node.data == data:
                if current_node.next == self.endnode:
                    self.remove_last()
                else:
                    current_node.data = current_node.next.data
                    current_node.next = current_node.next.next
                return True

            current_node = current_node.next
        

    def delete_all_occurrences(self, data):
        """
        Deletes all nodes with the specified data from the linked list.
        
        Returns:
            int: The number of deleted nodes.
        """
        count = 0
        current_node = self.head
        while True:
            if current_node == self.endnode:
                return count
            if current_node.data == data:
                if current_node.next == self.endnode:
                    self.remove_last()
                    count += 1
                    return count
                else:
                    current_node.data = current_node.next.data
                    current_node.next = current_node.next.next
                    count += 1
                    continue #cant advance after deletion

            current_node = current_node.next

    def __getitem__(self, index: int):
        """
        Returns the data stored at the specified index (0-based).
        
        Raises:
            IndexError: If the index is out of range.
        """
        actual_node = self.head
        i = 0
        while actual_node != self.endnode:
            if i == index:
                return actual_node.data
            actual_node = actual_node.next
            i += 1
        raise IndexError("Index out of range.")

    def __setitem__(self, index: int, data):
        """
        Sets the data at the specified index (0-based).
        
        Raises:
            IndexError: If the index is out of range.
        """
        actual_node = self.head
        i = 0
        while actual_node != self.endnode:
            if i == index:
                actual_node.data = data
                return 
            actual_node = actual_node.next
            i += 1
        raise IndexError("Index out of range.")

    def __iter__(self):
        """
        Returns a Python iterator for the linked list.
        """
        return LinkedListIterator(self.head,self.endnode)

    def a__iter__(self):
        """
        Returns a Python iterator for the linked list.
        """
        actual_node = self.head
        while actual_node != self.endnode:
            yield actual_node.data
            actual_node = actual_node.next
    
    def find_iter(self, data) -> "PositionIterator":
        """
        Returns an iterator pointing to the first occurrence of the specified data.
        """
        actual_node = self.head
        while actual_node != self.endnode:
            if actual_node.data == data:
                return PositionIterator(self, actual_node)
            actual_node = actual_node.next
        return PositionIterator(self, self.endnode)

    def start_iter(self) -> "PositionIterator":
        """
        Returns an iterator pointing to the first element of the list.
        """
        return PositionIterator(self, self.head)
    
    def end_iter(self) -> "PositionIterator":
        """
        Returns an iterator pointing to the sentinel node (endnode).
        """
        return PositionIterator(self, self.endnode)

    def selection_sort(self):
        current_node = self.head
        while True:
            if current_node == self.endnode:
                return
            min: int = current_node.data
            min_i: Node = current_node
            i: Node = current_node.next
            while i != self.endnode:
                if i.data < min:
                    min_i = i
                    min = i.data
                i = i.next
            if min_i != current_node:
                current_node.data, min_i.data = min_i.data, current_node.data

            current_node = current_node.next
    
    def insertion_sort(self):
        current_node = self.head.next
        while True:
            if current_node == self.endnode:
                return
            i = self.head
            akumulator = current_node.data
            while (i != current_node) and (i.data <= akumulator):
                i = i.next
            
            if i != current_node: 
                j = current_node
                while j != i:
                    k = self.head
                    while k.next != j:
                        k = k.next
                    j.data = k.data
                    j = k
                i.data = akumulator
            current_node = current_node.next

    def quick_sort(self):
        """recursive version of quick sort"""
        sorted_lst = self._quick_sort(self)
        self.head = sorted_lst.head
        self.endnode = sorted_lst.endnode

    def _quick_sort(self, lst):
        if lst.is_empty() or lst.head.next == lst.endnode:
            return lst

        pivot = self._najdi_stred(lst)

        mensi, rovno, vetsi = self._rozdel(lst, pivot)

        mensi = self._quick_sort(mensi)
        vetsi = self._quick_sort(vetsi)

        final = LinkedList()
        for x in mensi:
            final.append(x)
        for x in rovno:
            final.append(x)
        for x in vetsi:
            final.append(x)

        return final

    def _najdi_stred(self, lst):
        i, j = lst.head, lst.head
        while j != lst.endnode:
            i = i.next
            j = j.next
            if j == lst.endnode:
                return i
            j = j.next
        return i
    
    def _rozdel(self, lst, i_pivot: Node):
        """rozdělení seznamu podle pivotu na dvě části"""
        mensi = LinkedList()
        vetsi = LinkedList()
        rovno = LinkedList()

        aktualni: Node = lst.head
        while aktualni != lst.endnode:
            if aktualni.data > i_pivot.data:
                vetsi.append(aktualni.data)
            elif aktualni.data < i_pivot.data:
                mensi.append(aktualni.data)
            else:
                rovno.append(aktualni.data)
            aktualni = aktualni.next
        return mensi, rovno, vetsi


            
            

    
class LinkedListIterator:
    """
    Python-style iterator for the LinkedList class.

    This iterator follows the Python iterator protocol and is used in for-loops
    """

    def __init__(self, head: Node, endnode: Node):
       """
       Initializes the iterator with the starting node and the sentinel node (endnode) marking the end of the list.
       """        
       self.actual = head
       self.endnode = endnode
    
    def __iter__(self):
        """ Returns the iterator object itself (required by the iterator protocol)."""
        return self

    def __next__(self):
        """
        Returns the next data element in the list.
        
        Raises:
            StopIteration: If the iterator reaches the sentinel node (endnode).
        """
        if self.actual == self.endnode:
            raise StopIteration()
        data = self.actual.data
        self.actual = self.actual.next
        return data


class PositionIterator:
    """Custom STL-like iterator representing a position inside the linked list."""
    def __init__(self, linked_list, node: Node):
        """
        Initializes the iterator with a reference to the linked list and a node representing the current position.
        """
        self.linked_list = linked_list
        self.actual_node = node

    def __eq__(self, __value: object):
        """Checks whether two iterators represent the same position."""
        return isinstance(__value, PositionIterator) and self.actual_node == __value.actual_node and self.linked_list == __value.linked_list
    
    def get_value(self):
        """Returns the value stored at the current iterator position.
           
           Raises:
               ValueError: If the iterator points to the sentinel node (endnode).
        """
        if self.actual_node == self.linked_list.endnode:
            raise ValueError()
        return self.actual_node.data
    
    def set_value(self, data):
        """Sets the value at the current iterator position.
        
           Raises:
               ValueError: If the iterator points to the sentinel node (endnode).
        """
        if self.actual_node == self.linked_list.endnode:
            raise ValueError()
        self.actual_node.data = data
    
    def move_to_next(self):
        """Moves the iterator to the next position in the linked list.
        
        Raises:
               ValueError: If the iterator points to the sentinel node (endnode).
        """
        if self.actual_node == self.linked_list.endnode:
            raise ValueError()
        self.actual_node = self.actual_node.next

def simple_test_linked_list(sort_function, data):
    import random

    def build_list(a):
        lst = LinkedList()
        for x in a:
            lst.append(x)
        return lst

    def single(a):
        lst = build_list(a)
        sort_function(lst)
        result = list(lst)
        if result != sorted(a):
            print(f"{sort_function.__name__} error for: {a} with result: {result}")
            return False
        return True

    if not single(data):                       # original order
        return False
    if not single(sorted(data, reverse=True)): # descending order
        return False
    if not single(sorted(data)):               # ascending order
        return False

    for _ in range(10):
        shuffle_a = data[:]
        random.shuffle(shuffle_a)
        if not single(shuffle_a):              # random order
            return False

    return True


def sort_test_linked_list():
    algorithms = [LinkedList.selection_sort, LinkedList.quick_sort]

    a = [100, 2, 45, 13, 2, 90, 1, 3, 27]
    b = [100, 2, 45, 13, 2, 90, 1, 3, 27]
    c = [10]
    d = []

    for algorithm in algorithms:
        test_ok = simple_test_linked_list(algorithm, a)

        assert a == b, f"{algorithm.__name__}"  # input must not change

        if test_ok:
            test_ok = simple_test_linked_list(algorithm, c)
        if test_ok:
            test_ok = simple_test_linked_list(algorithm, d)
        if test_ok:
            print(f"Test on {algorithm.__name__} OK")


if __name__ == "__main__":
    """node = Node("A")
    print(node)

    lst = LinkedList()
    
    lst.append("1")
    lst.insert_at_beginning("A")
    lst.insert_at_beginning("B")
    lst.insert_at_beginning("C")
    lst.append("2")
    lst.display()
    print(lst)
    print(str(lst.first()))
    print(str(lst.last()))
    print(str(lst.remove_first()))
    print(str(lst.remove_last()))
    print(lst.find("A"))
    print(lst) #removes the same one withougt first and last nodes
    lst.__setitem__(0, "A")
    print(lst)
    print(lst.delete_all_occurrences("A"))
    print(lst)
    print(lst.delete("1"))
    print(lst)
    print(lst.delete("A"))"""

sort_test_linked_list()

def test():
    n = Node("John")
    print(n)

    l = LinkedList()
    for i in range(10):
        l.append(i)
    print(l)



    # Indexation ... setitem, getitem
    """
    print(l[1])
    l[1] = 12
    print(l)
    """
    
    # Python iterator:
    '''
    for x in l:
        print(x)
    '''

    # Position iterator (STL-like usage):
    '''
    it = l.start_iter()
    end = l.end_iter()

    while it != end:
        print(it.get_value())
        # it.set_value(it.get_value() * 2)
        it.move_to_next()
    '''

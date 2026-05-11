import copy


class Node:
    """Represents a node in a binary search tree."""

    def __init__(self, data=None):
        self.data = data    # Data contained within the node
        self.left = None    # Reference to the left child Node
        self.right = None   # Reference to the right child Node

    def __str__(self) -> str:
        """Return string representation of the node."""
        return str(self.data)

class BinarySearchTree:
    """
    Represents a Binary Search Tree.
    
    For every node:
    left subtree values < node.data < right subtree values
    """

    def __init__(self):
        """Initializes an empty binary search tree."""
        self.root = None   # Reference to the root node

    def is_empty(self) -> bool:
        """Returns True if the BST is empty, False otherwise."""
        return self.root is None

    def find(self, data):
        """
        Search for a node with the given data. Implement without recursion.

        Parameters:
            data: Data to search for.

        Returns:
            Node with the given data if found, otherwise None.
        """
        if self.is_empty():
            return None
        
        actual_node = self.root
        while actual_node != None:
            if actual_node.data == data:
                return actual_node
            elif actual_node.data > data:
                actual_node = actual_node.left
            elif actual_node.data < data:
                actual_node = actual_node.right

    def recursive_find(self, data):
        """
        Search for a node with the given data. Implement with recursion.

        Parameters:
            data: Data to search for.

        Returns:
            Node with the given data if found, otherwise None.
        """
        if self.is_empty():
            return None
        
        return self.find_r(data, self.root)

    def find_r(self, data, actual_node):
        if actual_node == None:
            return None
        if actual_node.data == data:
            return actual_node
        elif actual_node.data > data:
            return self.find_r(data, actual_node.left)
        elif actual_node.data < data:
            return self.find_r(data, actual_node.right)
        

    def insertR(self, data) -> None:
        """
        Insert a new node into the BST. If a node with the given data already exists, 
        do nothing. Implement without/with recursion.

        Parameters:
            data: Data to store in the BST.
        """
        self.root = self._insert_to_subtree(self.root, data)

    def _insert_to_subtree(self, subtree_root, data):
        if subtree_root is None:
            return Node(data)
        if subtree_root.data > data:
            subtree_root.left = self._insert_to_subtree(subtree_root.left, data)
        if subtree_root.data < data:
            subtree_root.right = self._insert_to_subtree(subtree_root.right, data)
        return subtree_root 

    def insert(self, data) -> None:
        """
        Insert a new node into the BST. If a node with the given data already exists, 
        do nothing. Implement without/with recursion.

        Parameters:
            data: Data to store in the BST.
        """
        actual_node = self.root
        if self.root is None:
            self.root = Node(data)
            return
        while True:
            if actual_node.data == data:
                return 
            elif actual_node.data < data:
                if actual_node.right is None:
                    actual_node.right = Node(data)
                    return
                else:
                    actual_node = actual_node.right
            elif actual_node.data > data:
                if actual_node.left is None:
                    actual_node.left = Node(data)
                    return
                else:
                    actual_node = actual_node.left         

    def print(self):
        self._print(self.root)
        print()

    def _print(self, subtree_root):
        if subtree_root is None:
            return
        print(subtree_root.data, end = " ")
        self._print(subtree_root.left)
        self._print(subtree_root.right)

    def print_inorder(self) -> None:
        """
        Print all elements in the BST in ascending order (inorder traversal).

        Example output: 2, 8, 10
        """
        self._print_inorder(self.root)
        print()

    def _print_inorder(self, subtree_root):
        if subtree_root is None:
            return
        
        self._print_inorder(subtree_root.left)
        print(subtree_root.data, end = " ")
        self._print_inorder(subtree_root.right)
        

    def print_structure(self) -> None:
        """
        Print the BST structure (each node on a separate line)
        with indentation reflecting tree depth.

        The traversal order (preorder, inorder, or postorder) is optional.

        Example output (for inorder traversal):

                4
            6
        7
                10
            18
                24
        """
        self._print_structure(self.root, 0)
        print()

    def _print_structure(self, subtree_root, depth):
        if subtree_root is None:
            return
              
        self._print_structure(subtree_root.left, depth + 1)
        print(depth*"   ", subtree_root.data) 
        self._print_structure(subtree_root.right, depth + 1)
 
    def delete_all(self) -> None:
        """
        Delete all nodes in the BST.

        Implement using recursion (postorder traversal) and the del statement.
        """
        
        self._delete_subtree(self.root)
        self.root = None

    def _delete_subtree(self, subtree_root):
        if subtree_root is None:
            return
              
        self._delete_subtree(subtree_root.left)
        self._delete_subtree(subtree_root.right)
        del subtree_root


    def copy(self) -> "BinarySearchTree":
        """
        Return a deep copy of the BST.

        Implement using recursion. Preorder

        Returns:
            A new BinarySearchTree containing copies of all nodes.
        """
        copy_tree = BinarySearchTree()
        if self.is_empty():
            return copy_tree
        copy_tree.root = self._copy(self.root)
        return copy_tree

    def _copy(self, subtree_root: Node):
        left, right = None, None
        if subtree_root.left is not None:
            left = self._copy(subtree_root.left)
        if subtree_root.right is not None:
            right = self._copy(subtree_root.right)
        node = Node()
        node.left, node.right, node.data = left, right, subtree_root.data
        return node


    def delete(self, data) -> None:
        """
        Delete a node with the given data if it exists.

        Parameters:
            data: Data of the node to delete.
        """
        ...

    def count(self) -> int:
        """
        Return the number of nodes in the BST.

        Implement using recursion. Preorder
        """
        if self.is_empty():
            return 0

        return self._count(self.root)

    
    def _count(self, subtree_root: Node) -> int:
        left, right = 0, 0
        if subtree_root.left is not None:
            left = self._count(subtree_root.left)
        if subtree_root.right is not None:
            right = self._count(subtree_root.right)
        return (left + right + 1)
        
    def depth(self) -> int:
        """
        Return the depth of the BST.

        Implement using recursion.

        Returns:
            Depth (height) of the tree.
        """
        if self.is_empty():
            return 0
        
        return self._depth(self.root)
    
        
    def _depth(self, subtree_root) -> int:
        left, right = 0, 0
        if subtree_root.left is not None:
            left = self._depth(subtree_root.left)
        if subtree_root.right is not None:
            right = self._depth(subtree_root.right)
        return (max(left, right) + 1)


    def find_min(self):
        """
        Find and return the node with the smallest data in the BST.

        Implement without recursion.

        Returns:
            Node with the smallest data, or None for an empty BST.
        """
        if self.is_empty():
            return None
        
        actual_node = self.root
        while True:
            if actual_node.left is None:
                return actual_node
            else:
                actual_node = actual_node.left


    def serialize_to_list(self) -> list:
        """
        Preorder serialization: convert the BST to a list representation
        using preorder traversal.

        Returns:
            A list of data values stored in the BST.
        """
        ...

    @staticmethod
    def reconstruct_from_list(input_list: list) -> "BinarySearchTree":
        """
        Deserialize a BST from the list representation produced
        by serialize_to_list().

        The internal structure of the reconstructed tree must be
        the same as the original one.

        Parameters:
            input_list: List produced by serialize_to_list().

        Returns:
            Reconstructed BinarySearchTree.
        """
        ...

    #########################################################

    def print_by_levels_recursive(self) -> None:
        """
        Print nodes level by level (level-order traversal).
        Nodes at the same depth are printed on the same line.

        Implement breadth-first traversal using recursive
        depth-first traversal.

        BONUS: Indent output to reflect tree structure.

        Example output:

               7
          3       16
        1   6      25
        """
        ...

    def print_by_levels_queue(self) -> None:
        """
        Print BST data by levels (each level on a separate line)
        using a queue.

        Implement breadth-first traversal non-recursively.

        Use the Queue class from a previous assignment.

        BONUS: Indent output to reflect tree structure.
        """
        ...

    def print_preorder_stack(self) -> None:
        """
        Print BST nodes in preorder (each node on a new line).

        Implement depth-first traversal using a stack.

        Use the Stack class from a previous assignment.

        BONUS: Indent output based on tree depth.
        """
        from collections import deque
        stack = deque()
        if self.root is not None:
            stack.append(self.root)
        while len(stack) > 0:
            actual_node = stack.pop()
            print(actual_node.data)
            if actual_node.right is not None:
                stack.append(actual_node.right)
            if actual_node.left is not None:    
                stack.append(actual_node.left)

    #########################################################

    @staticmethod
    def from_ordered_list_r(input_list: list) -> "BinarySearchTree":
        """
        Construct a balanced BST from a sorted list.

        Time complexity: O(n).

        Parameters:
            input_list: List of data sorted in ascending order.

        Returns:
            A balanced BinarySearchTree containing the elements.
        """
        tree = BinarySearchTree()
        tree.root = BinarySearchTree._from_ordered_list_r(input_list, 0, len(input_list) - 1)
        return tree
        
    @staticmethod
    def _from_ordered_list_r(input_list: list, od: int, do: int):
        if od > do:
            return None
        stred = (od + do) // 2
        koren = Node(input_list[stred])
        koren.left = BinarySearchTree._from_ordered_list_r(input_list, od, stred-1)
        koren.right = BinarySearchTree._from_ordered_list_r(input_list, stred+1, do)
        return koren 


if __name__ == "__main__":
    '''tree = BinarySearchTree()
    for x in [23, 12, 40, 17, 30, 15, 35]:
        tree.insertR(x)
    tree.print()
    tree.print_inorder()
    tree.print_structure()
    #tree.delete_all()
    tree.print_preorder_stack()
    
    print("\nfind():")
    node = tree.find(17)
    print("Find 17:", node.data if node else None)

    node = tree.find(99)
    print("Find 99:", node.data if node else None)

    print("\nrecursive_find():")
    node = tree.recursive_find(30)
    print("Find 30:", node.data if node else None)

    node = tree.recursive_find(100)
    print("Find 100:", node.data if node else None)

    print("\nfind_min():")
    min_node = tree.find_min()
    print("Min value:", min_node.data if min_node else None)

    print("\ncount():")
    print("Number of nodes:", tree.count())

    print("\ndepth():")
    print("Tree depth:", tree.depth())

    print("\ncopy():")
    copied_tree = tree.copy()

    print("Original tree (inorder):")
    tree.print_inorder()

    print("Copied tree (inorder):")
    copied_tree.print_inorder()'''

    #postaveí binárního stromu z seznamu
    sorted_list = [10, 20, 30, 40, 50, 60, 70]
    tree = BinarySearchTree.from_ordered_list_r(sorted_list)

    tree.print_inorder()   # should print sorted order
    tree.print_structure() # shows balanced structure

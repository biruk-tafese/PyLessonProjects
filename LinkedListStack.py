from SinglylinkedList import Node

class Stack:
    def __init__(self):
     
        """
        Initialize the empty stack.
        """
        #Top element
        self.top = None

    def push(self, element):

        """
         Pushes an element onto the top of the stack.

        """
        #Create a new node
        node = Node(element)
        #make the new node the top element
        node.next = self.top
        self.top = node

    def pop(self):

        """
        Removes and returns the top element from the stack. 

        """
        if self.is_empty():
            raise Exception("Stack is empty")
        element = self.top.data

        #removes the top element
        self.top = self.top.data
        return element
    
    def peek(self):

        """
        Returns the top element of the stack is without removing it.

        """
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.top.data
    
    def is_empty(self):

        """
         Checks if the stack is empty.
        """
        return self.top is None
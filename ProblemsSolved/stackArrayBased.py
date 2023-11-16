
class Stack:
    def __init__(self, size):
        """
        Initialize the stack with a given size.
        """
        #Array to store the elements
        self.data = [0]*size
        #Index of the top element
        self.top = -1

    def push(self, element):
        """
         Pushes an element onto the top of the stack.
        """
        if self.is_full():
            print("Stack is full.")
            return
        #Increment top and add element
        self.top += 1
        self.data[self.top] = element
        

    def pop(self):
        """
         Removes an return the top element from the stack.

        """
        element = self.data[self.top]
        #Decrement top which cause the element to be removed
        self.top = -1
        return element
    
    
    def peek(self):
        """
         Returns the top element of the stack without removing it.

        """
        if self.is_empty():
            raise Exception("Stack is Empty")
        return self.data[self.top]
    
    
    def is_full(self):
        """
         Checks if the stack is full.
        """
        return self.top == len(self.data) -1
    
    
    def is_empty(self):
        """
        Checks if the stack is empty. 
        """
        return self.top == -1
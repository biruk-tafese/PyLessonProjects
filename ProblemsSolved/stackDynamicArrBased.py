
class DynamicArrayBased:
    def __init__(self):
        """
         Initialize the empty stack.

        """
        self.data = []

    def push(self, item):
        """
         Adds an item to the top of the stack.

        """
        self.data.append(item)

    def pop(self):
        """
         Removes and return the top item fron the stack.

        """
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.data.pop()
    
    def peek(self):
        """
        Returns the top item from the stack without removing it.

        """
        if self.is_empty(self):
            raise Exception("Stack is empty")
        return self.data[-1]
    
    def is_empty(self):
        """
        checks if the stack is empty.

        """
        return len(self.data) == 0

        

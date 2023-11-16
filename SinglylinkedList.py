
class Node:
    def __init__(self, data):
        self.data = data
        self.next  = None

    
class LinkedList:
    def __init__(self):
        self.head = None
    

    def is_empty(self):
        # for empty

       return self.head is None 
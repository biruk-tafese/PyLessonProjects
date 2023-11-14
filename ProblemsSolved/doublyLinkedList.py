class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class DoubelEndedLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None
    

    def insert_last(self, value):
        """
        Insert new Node with the specified value at the end of the list

        """
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        
        else:
            #update the tails next reference
            #and tail reference
            self.tail.next = new_node
            self.tail = new_node

    def delete_last(self):
        """
        Deletes and returns the last node from this list. If the list is empty, returns None.
        """
        if self.is_empty():
            return None
        
        deleted_node = self.tail

        #If there's only one node in the list
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            #Find the second last noe in the list
            pred = self.head
            while pred.next != self.tail:
                pred = pred.next
            #update the second last node's next
            #reference and the tail reference
            pred.next = None
            self.tail = pred

        return deleted_node
     

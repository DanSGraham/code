"""A custom implementation of a linked list for practice with the data type"""

#TODO (DAN): Add remove by value, remove by index, remove by pop.
#TODO (DAN): Add add by index (works by iteration, like if there was only  a head).
#TODO (DAN): Add return by index, value or peek
#TODO (DAN): Implement doubly linked version.


class LLNode(object):
    """Designed to store data and link in a single way."""

    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class LinkedList(object):
    """Custom Linked list implementation"""

    def __init__(self):
        self.head = None
        self.tail = None

    def addTail(linkNode):
        if not self.head:
            self.head = linkNode
            self.tail = self.head

        else:
            self.tail.next = linkNode
            self.tail = linkNode

    def addHead(linkNode):
        tmp = self.head
        self.head = linkNode
        self.head.next = tmp
        if not self.tail:
            self.tail = tmp

    def add(linkNode, index):
        prev = self.head
            
            

    def popHead():
        tmp = self.head
        if tmp:
            self.head = self.head.next
        return tmp

    

    



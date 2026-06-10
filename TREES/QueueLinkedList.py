# A Node is a single box that holds a value and points to the next box
class Node:
    def __init__(self, value):
        self.value = value   # the actual data stored in this box
        self.next = None     # points to the next node (empty at first)


# A Queue works like a line of people:
# - new people join at the BACK (enqueue)
# - people leave from the FRONT (dequeue)
# - First person in = First person out (FIFO)
class Queue:
    def __init__(self):
        self.head = None  # front of the line
        self.tail = None  # back of the line


    # isEmpty: checks if the queue has no one in line
    def isEmpty(self):
        if self.head is None:
            return True
        return False


    # enqueue: adds a new person to the BACK of the line
    def enqueue(self, value):
        newNode = Node(value)         # create a new box with the value
        if self.tail is None:         # if the line is empty
            self.head = newNode       # this new box is both front and back
            self.tail = newNode
        else:
            self.tail.next = newNode  # current last box points to the new box
            self.tail = newNode       # new box is now the last in line


    # dequeue: removes and returns the person at the FRONT of the line
    def dequeue(self):
        if self.isEmpty():
            return None
        
        nodeToRemove = self.head          # grab the front box
        self.head = self.head.next        # move front pointer to the next box
        if self.head is None:             # if line is now empty
            self.tail = None              # back pointer should also be empty
        nodeToRemove.next = None          # disconnect the removed box
        return nodeToRemove               # return the removed box


    # peek: look at the front value WITHOUT removing it
    def peek(self):
        if self.isEmpty():
            return None
        return self.head
    

    # delete: empties the entire queue
    def delete(self):
        self.head = None
        self.tail = None
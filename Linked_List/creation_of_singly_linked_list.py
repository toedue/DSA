# Step 2: Create a Node class
class Node:
    def __init__(self, value=None):
        self.value = value               # value stores the data of the node
        self.next = None                 # next stores the reference (link) to the next node


# Step 1: Create a Singly Linked List class
class SLinkedlist:
    def __init__(self):
        self.head = None                             # head points to the first node in the linked list (initially the list is empty so it is None)
        self.tail = None                             # tail points to the last node in the linked list (initially it is also None because the list is empty)

# Step 3: Create an object of the linked list
singlyLinkedList = SLinkedlist()

node1 = Node(1)                  # Create the first node with value 1
node2 = Node(2)                  # Create the second node with value 2

singlyLinkedList.head  = node1              # Set node1 as the first node (head) of the linked list
singlyLinkedList.head.next = node2          # Connect node1 to node2 using the next pointer
singlyLinkedList.tail = node2               # Set node2 as the last node (tail) of the linked list


# Time Complexity: O(1)
# All operations above (creating nodes, assigning head/tail, linking nodes)
# take constant time because they do not depend on the size of the list. 
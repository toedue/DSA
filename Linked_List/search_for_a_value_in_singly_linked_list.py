# Node class represents a single element in the linked list
class Node:
    def __init__(self, value=None):
        self.value = value              # Stores the data of the node
        self.next = None                # Points to the next node (initially None)

# Singly Linked List class
class SLinkedList:
    def __init__(self):
        self.head = None              # First node in the list                
        self.tail = None              # Last node in the list 

    # Iterator method (allows looping through the list)
    def __iter__(self):
        node = self.head                # Start from the head
        while node:                     # Continue until node becomes None
            yield node                  # Return current node
            node = node.next            # Move to next node

    # Method to insert a node at a specific location
    def insertSLL(self, value, location):
        newNode = Node(value)           # Create a new node with given value

        # Case 1: If the list is empty
        if self.head is None:
            self.head = newNode         # New node becomes head
            self.tail = newNode         # New node also becomes tail

        else:
            # Case 2: Insert at the beginning (location = 0)
            if location == 0:
                newNode.next = self.head        # New node points to current head
                self.head = newNode             # Update head to new node

            # Case 3: Insert at the end (location = 1)
            elif location == 1:
                newNode.next = None             # New node will be last node
                self.tail.next = newNode        # Current tail points to new node
                self.tail = newNode            # Update tail

            # Case 4: Insert at a specific position (middle)
            else:
                tempNode = self.head        # Start from head
                index = 0

                # Traverse until the position before the desired location
                while index < location -  1:
                    tempNode = tempNode.next
                    index += 1

                nextNode = tempNode.next        # Store next node
                tempNode.next = newNode         # Link previous node to new node
                newNode.next = nextNode


    # Traverse    
    def traverseSLL(self):
        # Check if the linked list is empty
        if self.head is None:
            print("The Singly Linked List does not exist")
        else:
            node = self.head             # Start traversal from the head (first node)

            # Loop through the list until we reach the end (node becomes None)
            while node is not None:
                print(node.value)       # Print the value of the current node
                node = node.next        # Move to the next node


    # Search for a node in Singly Linked List
    def searchSLL(self, nodeValue):

        # Check if the list is empty
        if self.head is None:
            return "The list does not exist"
        else:
            node = self.head            # Start from the head (first node)

            # Traverse through the list
            while node is not None:

                # Check if current node's value matches the search value
                if node.value == nodeValue:
                    return node.value       # Value found → return it
                node = node.next            # Move to the next node

            # If loop finishes and value not found
            return "The value does not exist in this list"
                





# Create list
singlyLinkedList = SLinkedList()
singlyLinkedList.insertSLL(1, 1)
singlyLinkedList.insertSLL(2, 1)
singlyLinkedList.insertSLL(3, 1)
singlyLinkedList.insertSLL(4, 1) 

singlyLinkedList.insertSLL(0, 0) 

singlyLinkedList.insertSLL(0, 3)
singlyLinkedList.insertSLL(0, 4)

print([node.value for node in singlyLinkedList]) 


# singlyLinkedList.traverseSLL()

print(singlyLinkedList.searchSLL(33))
# TreeNode represents a single node in a Binary Tree
# Each node holds data and has at most two children: left and right
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None   # Points to the left subtree (initially empty)
        self.rightChild = None  # Points to the right subtree (initially empty)



# Build a small binary tree manually:
#        Drinks
#       /      \
#     Hot      Cold

newBT = TreeNode("Drinks")       # Root node
leftChild = TreeNode("Hot")      # Left child of root
tea = TreeNode("Tea")
coffee = TreeNode("Coffee")  
leftChild.leftChild = tea
leftChild.rightChild = coffee    
rightChild = TreeNode("Cold")    # Right child of root

newBT.leftChild = leftChild      # Attach Hot  to the left  of Drinks
newBT.rightChild = rightChild    # Attach Cold to the right of Drinks


# Pre-order Traversal: visits nodes in Root → Left → Right order
# This means the root is always printed before its children
#
# Time Complexity:  O(n) — every node is visited exactly once
# Space Complexity: O(h) — call stack depth equals the height of the tree
#                   O(log n) for a balanced tree, O(n) worst case (skewed tree)
def preOrderTraveral(rootNode):
    if not rootNode:   # Base case: if the node is None, stop recursion
        return
    
    print(rootNode.data)                    # 1. Visit root  → prints: Drinks, Hot, Cold
    preOrderTraveral(rootNode.leftChild)    # 2. Recurse left subtree
    preOrderTraveral(rootNode.rightChild)   # 3. Recurse right subtree

# Output:
# Drinks
# Hot
# Cold
preOrderTraveral(newBT)



# In-order Traversal: visits nodes in Left → Root → Right order
# Commonly used in Binary Search Trees because it prints values in sorted order
#
# Time Complexity:  O(n) — every node is visited exactly once
# Space Complexity: O(h) — call stack depth equals the height of the tree
#                   O(log n) balanced tree, O(n) worst case (skewed tree)
def inOrderTraveral(rootNode):
    if not rootNode:   # Base case: if the node is None, stop recursion
        return
    
    inOrderTraveral(rootNode.leftChild)  # 1. Recurse all the way down the left side first
    print(rootNode.data)                 # 2. Only print AFTER the entire left is done
    inOrderTraveral(rootNode.rightChild) # 3. Then recurse down the right side

# Output:
# Hot
# Drinks
# Cold
inOrderTraveral(newBT) 



# Post-order Traversal: visits nodes in Left → Right → Root order
# The root is always printed LAST (after all children are done)
# Commonly used when deleting a tree or calculating folder sizes
#
# Time Complexity:  O(n) — every node is visited exactly once
# Space Complexity: O(h) — call stack depth equals the height of the tree
#                   O(log n) balanced tree, O(n) worst case (skewed tree)
def postOrderTraversal(rootNode):
    if not rootNode:  # Base case: if the node is None, stop recursion
        return
    
    postOrderTraversal(rootNode.leftChild)   # 1. Recurse all the way down the left side first
    postOrderTraversal(rootNode.rightChild)  # 2. Then recurse all the way down the right side
    print(rootNode.data)                     # 3. Only print AFTER both children are fully done

# On our tree:
#        Drinks
#       /      \
#     Hot      Cold
#
# Output:
# Hot
# Cold
# Drinks

postOrderTraversal(newBT)
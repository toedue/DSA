class Node:
    def __init__ (self, data):
        self.data = data
        self.left = None
        self.right = None

# in order to avoid confusion around what we are considering an officual tree may be add metadata or helper functions
# make a simple wrapper class 
class Tree:
    def __init__ (self, root, name=""): # takes a root node
        self.root = root
        self.name = name

node = Node(10)

node.left = Node(5)
node.right = Node(15)

node.left.left = Node(2)
node.left.right = Node(6)

node.right.left = Node(13)
node.right.right = Node(10000)

# to see data at a particular point or node in the tree
# print(node.right.data)
# print(node.right.right.data)


# take any node and declare it to be its own tree
# myTree = node.left

# myTree is whole new tree into itself and node.left is the root of the tree


# 

myTree = Tree(node, "abudy's tree")

print(myTree.name)
print(myTree.root.left.data)
print(myTree.root.right.right.data)












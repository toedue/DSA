class Node:
    def __init__ (self, data):
        self.data = data
        self.left = None
        self.right = None

    def search(self, target):
        if self.data == target:
            print("Found it!")
            return self   #returning the node that we found in the tree
        
        # if we dont  we match it we need to keep looking
        if self.left and self.data > target:
            return self.left.search(target) # recursively keep searching the tree
        
        if self.right and self.data < target:
            return self.right.search(target)
        
        print("value is not in the tree")


class Tree:
    def __init__ (self, root, name=""): # takes a root node
        self.root = root
        self.name = name

    def search(self, target):
        return self.root.search(target)

node = Node(10)

node.left = Node(5)
node.right = Node(15)

node.left.left = Node(2)
node.left.right = Node(6)

node.right.left = Node(13)
node.right.right = Node(10000)


myTree = Tree(node, "abudy's tree")

found = myTree.search(10000)
print(found.data)



# TreeNode class represents a single node in a general tree (each node can have multiple children)
class TreeNode:
    # data: the value stored in the node
    # children: list of child TreeNode objects (defaults to empty list)
    def __init__(self, data, children = []):
        self.data = data
        self.children = children

    # Recursively builds a string representation of the tree with indentation showing depth
    def __str__(self, level=0):
        ret = " " * level + str(self.data) + "\n"
        for child in self.children:
            ret += child .__str__(level + 1)
        return ret
    
    # Appends a child node to this node's children list
    def addChild(self, TreeNode):
        self.children.append(TreeNode)


# Root node of the tree
tree = TreeNode("Drinks", [])

# Two main category nodes (level 1)
cold = TreeNode("cold", [])
hot = TreeNode("Hot", [])

# Attach both categories to the root
tree.addChild(cold)
tree.addChild(hot)

# Leaf nodes for hot drinks (level 2)
tea = TreeNode("tea", [])
coffee = TreeNode("coffee", [])

# Leaf nodes for cold drinks (level 2)
cola = TreeNode("cola", [])
fanta = TreeNode("fanta", [])

# Add cola and fanta under cold
cold.addChild(cola)
cold.addChild(fanta)

# Note: coffee is created but never added — and tea is added twice (likely a bug)
hot.addChild(tea)
hot.addChild(tea)

# Print the full tree structure using __str__
print(tree)
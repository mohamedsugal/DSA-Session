class TreeNode:
    def __init__(self,value,weight):
        self.value = value
        self.left = None
        self.right = None
        self.weight = weight

def print_tree(tree):
    if not tree:
        return

    print(tree.value,tree.weight)
    print_tree(tree.left)
    print_tree(tree.right)


tree = TreeNode("Seattle",0)
tree.left = TreeNode("Denver",1305)
tree.right = TreeNode("New York",2401)
tree.left.left = TreeNode("Miami",2064)
tree.left.right = TreeNode("Los Angels",1016)
tree.left.right.left = TreeNode("Dallas",1435)
tree.left.right.left.right = TreeNode("Minneapolis",990)
tree.right.right = TreeNode("Boston",2016)

print_tree(tree)
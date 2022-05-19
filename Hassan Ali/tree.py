class TreeNode:
    def __init__(self,value,distance):
        self.value = value
        self.left = None
        self.right = None
        self.distance = distance

# printing using inorder
def print_tree(tree):
    if not tree:
        return
    print(tree.value,tree.weight)
    print_tree(tree.left)
    print_tree(tree.right)

# 
def get_path(root,city):
  
    def helper(node,path,city,dist1):
        
        if not node: return
        path.append(node.value) 
        if city == node.value or helper(node.left,path,city,dist1) or helper(node.right,path,city,dist1):   
            dist1.append(node.distance)
            return True
        path.pop()
        return False

    paths = []
    dist_count = []
    helper(root,paths,city,dist_count)

    res = ""
    for p in paths:
         res += p + " -> "

    print("distance travelled is ",sum(dist_count))

    return res


tree = TreeNode("Seattle",0)
tree.left = TreeNode("Denver",1305)
tree.right = TreeNode("New York",2401)
tree.left.left = TreeNode("Miami",2064)
tree.left.right = TreeNode("Los Angels",1016)
tree.left.right.left = TreeNode("Dallas",1435)
tree.left.right.left.right = TreeNode("Minneapolis",990)
tree.right.right = TreeNode("Boston",2016)

# print_tree(tree)

print(get_path(tree,"Dallas"))

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
def inorder(root):
    if not root:
        return None
    inorder(root.left)
    print(root.val, end="->")
    inorder(root.right)

def areTheyCousins(root, person1, person2):
    map = {}
    def dfs(root, parent, depth, person1, person2):
      if not root:
        return False
      
      dfs(root.left, root, depth + 1, person1, person2)
      dfs(root.right, root, depth + 1, person1, person2)
      
      if root.val in (person1, person2):
        map[root.val] = (parent, depth)
    
    dfs(root, None, 0, person1, person2)

    return person1 in map and person2 in map and map[person1][0] != map[person2][0] and map[person1][1] == map[person2][1]
    

root = TreeNode("Omar")
root.left = TreeNode("Jama")
root.right = TreeNode("Gedi")
root.left.left = TreeNode("Abdi")
root.right.right = TreeNode("Nimo")

# inorder(root)

cousins = areTheyCousins(root, "Abdi", "Gedi")
print(cousins) # False
cousins = areTheyCousins(root, "Jama", "Gedi")
print(cousins) # False
cousins = areTheyCousins(root, "Abdi", "Nimo")
print(cousins) # True
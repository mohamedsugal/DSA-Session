"""
                    Seattle
                  /        \
              Denver     New York
            /      \           \
        Miami   Los Angeles   Boston
                 /
             Dallas
                \
            Minneapolis

1. Find the path from Seattle to Dallas?
2. Find the distance from Seattle to Minneapolis?
3. Find the distance from Seattle to Dallas?

(3) What about Seattle to Dallas?
"""


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.right = None
    self.left = None

def path_cities(root, city):
  paths = []
  helperPath_cities(root, paths, city)
  return "->".join(paths)

def helperPath_cities(root, paths, city):
  if not root:
    return False
  paths.append(root.val)
  if city in paths:
    return True
  if not root.left and not root.right and root.val != city:
    paths.pop(-1)
    return False
  return helperPath_cities(root.left, paths, city) or helperPath_cities(root.right, paths, city)

def find_distance(root, city):
  sum = [0]
  find_distance_helper(root, sum, city)
  return sum[0]

def find_distance_helper(root, sum, city):
    pass
  
  
tree = TreeNode("seattle")
tree.left = TreeNode("Denver")
tree.right = TreeNode("New york")
tree.left.left = TreeNode("Miami")
tree.left.right = TreeNode("Los Angeles")
tree.right.right = TreeNode("Boston")
tree.left.right.left = TreeNode("Dallas")
tree.left.right.left.right = TreeNode("Minneapolis")


print(path_cities(tree, "Dallas"))
# output: seattle->Denver->Los Angeles->Dallas
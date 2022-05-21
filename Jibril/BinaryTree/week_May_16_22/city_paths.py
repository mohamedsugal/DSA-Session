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

"""


class TreeNode:
  def __init__(self, val, distance):
    self.val = val
    self.distance = distance
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
    if not root:
      return None
    sum[0] += root.distance
    if root.val == city:
      return True
    if not root.left and not root.right and root.val != city:
      sum[0] -= root.distance
      return False
    return find_distance_helper(root.left, sum, city) or find_distance_helper(root.right, sum, city)
  
  
tree = TreeNode("seattle", 0)
tree.left = TreeNode("Denver", 1305)
tree.right = TreeNode("New york", 2401)
tree.left.left = TreeNode("Miami", 2064)
tree.left.right = TreeNode("Los Angeles", 1016)
tree.right.right = TreeNode("Boston", 216)
tree.left.right.left = TreeNode("Dallas", 1435)
tree.left.right.left.right = TreeNode("Minneapolis", 990)


print(path_cities(tree, "Dallas"))
# output: seattle->Denver->Los Angeles->Dallas
print(find_distance(tree, "Minneapolis"))
print(find_distance(tree, "Dallas"))
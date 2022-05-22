"""
                    Seattle
                  /        \
              Denver     New York
            /      \           \
        Miami   Los Angeles   Boston
          /           /
      Columbus     Dallas
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
  if root.val == city or helperPath_cities(root.left, paths, city) or helperPath_cities(root.right, paths, city):
    return True
  paths.pop(-1)
  return False
  

# preorder itterative solution.
def path_cities_itter(root, city):
  stack = [root]
  paths = []
  while stack:
    node = stack.pop()
    if node.val == city:
      paths.append(node.val)
      return paths
    paths.append(node.val)
    if not node.right and not node.left:
      paths.pop(-1)
    if node.right:
      stack.append(node.right)
    if node.left:
      stack.append(node.left)
  return "->".join(paths)

def find_distance(root, city):
  sum = [0]
  find_distance_helper(root, sum, city)
  return sum[0]

def find_distance_helper(root, sum, city):
    if not root:
      return None
    sum[0] += root.distance
    if root.val == city or find_distance_helper(root.left, sum, city) or find_distance_helper(root.right, sum, city):
      return True

    sum[0] -= root.distance
    return False

def find_distance_itter(root, city):
  distance = 0
  stack = [root]
  while stack:
    node = stack.pop()
    if node.val == city:
      distance += node.distance
      return distance
    distance += node.distance
    if not node.right and not node.left and node.val != city:
      distance -= node.distance
    
    if node.right:
      stack.append(node.right)
    if node.left:
      stack.append(node.left)
  return distance
  
  
tree = TreeNode("seattle", 0)
tree.left = TreeNode("Denver", 1305)
tree.right = TreeNode("New york", 2401)
tree.left.left = TreeNode("Miami", 2064)
tree.left.left.left = TreeNode("Columbus", 2064)
tree.left.right = TreeNode("Los Angeles", 1016)
tree.right.right = TreeNode("Boston", 216)
tree.left.right.left = TreeNode("Dallas", 1435)
tree.left.right.left.right = TreeNode("Minneapolis", 990)


print(path_cities(tree, "Dallas"))
# output: seattle->Denver->Los Angeles->Dallas
print(find_distance(tree, "Minneapolis")) # 4746
print(find_distance(tree, "Dallas")) # 3756
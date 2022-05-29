from typing import Optional
class TreeNode:
  def __init__(self, val):
    self.val = val  
    self.left = None
    self.right = None
    
def sumOfLeftLeavesIter(self, root: Optional[TreeNode]) -> int:
        # iterative Solution
        left_nodes = 0
        stack = [(root, False)]
        
        while stack:
            root, isLeft = stack.pop()
            # process the root and isLeft
            if not root.left and not root.right and isLeft:
                left_nodes += root.val
            if root.right:
                stack.append((root.right, False))
            if root.left:
                stack.append((root.left, True))
        return left_nodes
        
def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
      if root and not root.right and not root.left:
          return 0
      sum_left_leaves = [0]
      self.dfs(root, sum_left_leaves)
      return sum_left_leaves[0]
  
def dfs(self, root, left_leaves):
    if not root:
        return None
    if not root.left and not root.right:
        left_leaves[0] += root.val
    self.dfs(root.left, left_leaves)
    # Don't call the function on the right side of the tree if the current node's right node is a leave node.
    if not (root.right and not root.right.left and not root.right.right):
        self.dfs(root.right, left_leaves)
  
        
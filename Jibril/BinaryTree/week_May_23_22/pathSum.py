from typing import Optional
class TreeNode:
  def __init__(self, val):
    self.val = val  
    self.left = None
    self.right = None
    
def hasPathSumIter(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root and targetSum == 0:
            return False
        
        stack = [(root, targetSum)]
        while stack:
            root, targetSum = stack.pop()
            if not root and targetSum != 0:
                return False
            targetSum -= root.val
            if not root.left and not root.right and targetSum == 0:
                return True
            if root.right:
                stack.append((root.right, targetSum))
            if root.left:
                stack.append((root.left, targetSum))
            
        return False
      
def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        targetSum -= root.val
        
        if not root.left and not root.right and targetSum == 0:
            return True
        
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)
     
        
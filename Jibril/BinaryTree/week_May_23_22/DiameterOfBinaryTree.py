from typing import Optional

class TreeNode:
    def __init__(self, val):
    self.val = val  
    self.left = None
    self.right = None
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
      diameter = [0]
        res = 0
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)

            diameter[0] = max(diameter[0], left+right)

            return max(left, right) + 1
        dfs(root)
        return diameter[0]
# 112. Path Sum

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        # base case
        if not root:
            return False
        
        # base case
        if not root.left and not root.right and root.val == targetSum:
            return True
        
        # decrement the targetsum
        targetSum -= root.val
        
        # recursive function
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)

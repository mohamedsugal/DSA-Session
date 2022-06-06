# 404. Sum of Left Leaves

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:n
        
        res = 0
        
        # base case
        if not root:
            return 0
        
        # edge case
        if root.left:
            if not root.left.left and not root.left.right:
                res +=  root.left.val
            else:
                res +=  self.sumOfLeftLeaves(root.left)
        
        # edge case
        if root.right:
            res +=  self.sumOfLeftLeaves(root.right)
        
        return res
            
            
                
            
            
            
        
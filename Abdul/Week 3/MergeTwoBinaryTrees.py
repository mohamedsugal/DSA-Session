# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]: 
        
        # base case
        if not root1 and not root2:
            return None
        
        # default val
        root1val = 0
        root2val = 0
        
        # corrected val
        if root1:
            root1val = root1.val
        
        # corrected val
        if root2:
            root2val = root2.val
        
        # calculations
        calculation = root1val + root2val
            
        # new tree
        tree = TreeNode(calculation)
        
        # recursive
        tree.left = self.mergeTrees(root1.left if root1 else None, root2.left if root2 else None)
        tree.right = self.mergeTrees(root1.right if root1 else None, root2.right if root2 else None)
        
        # return tree
        return tree
        
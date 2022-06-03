# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        
        self.CALCULATION = 0
        
        def helper(root,BOOlEAN):
            
            if not root:
                return
            
            if BOOlEAN:
                self.CALCULATION += root.val
                return 
            
            if root.val % 2 == 0:
                
                if root.left:
                    helper(root.left.left, True)
                    helper(root.left.right, True)
                
                if root.right:
                    helper(root.right.right, True)
                    helper(root.right.left, True)
            
            helper(root.right, False)
            helper(root.left, False)
        
        helper(root, False)
        
        return self.CALCULATION
    